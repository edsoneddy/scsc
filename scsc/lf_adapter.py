"""
BSD 3-Clause License

Copyright (c) 2020, Jean-Michel Begon
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

# Original author: Jean-Michel Begon
# Original repository: https://github.com/jean-michel-begon/locmoss

# File query.py
import os
from datetime import datetime, timedelta

class Query(object):
    def __init__(self, label=None):
        self.label = self.__class__.__name__ if label is None else label

    def header(self, report):
        report.add_header(self.label)

    def query_(self, report, invert_index):
        pass

    def __call__(self, invert_index):
        report = Report()
        self.header(report)
        self.query_(report, invert_index)
        return report


class MetaData(Query):
    __HEADER__ = """   __                 _             ___  __  __     __                       _
  / /  ___   ___ __ _| |   /\/\    /___\/ _\/ _\   /__\ ___ _ __   ___  _ __| |_
 / /  / _ \ / __/ _` | |  /    \  //  //\ \ \ \   / \/// _ \ '_ \ / _ \| '__| __|
/ /__| (_) | (_| (_| | | / /\/\ \/ \_// _\ \_\ \ / _  \  __/ |_) | (_) | |  | |_
\____/\___/ \___\__,_|_| \/    \/\___/  \__/\__/ \/ \_/\___| .__/ \___/|_|   \__|
                                                           |_|                   """
    def __init__(self, **context):
        super().__init__()
        self.dict = context
        self.creation = datetime.now()

    def duration_str(self, duration_in_sec):
        s = str(duration_in_sec)
        # remove milliseconds and stuff
        return s.split(".")[0]

    def header(self, report):
        for line in self.__HEADER__.split(os.linesep):
            report.add_raw(line)

    def query_(self, report, invert_index):
        now = datetime.now()
        with report.add_list("Context") as ls:
            for k,v in self.dict.items():
                ls.append("{}: {}".format(k, v))

            ls.append("Hash: {}".format(hash(invert_index)))
            ls.append("Duration: {}".format(self.duration_str(now - self.creation)))

class SoftwareList(Query):
    def query_(self, report, invert_index):
        softwares = invert_index.get_softwares()
        for sf in softwares:
            with report.add_list(sf.name) as report_list:
                report_list.extend(sf)

class CorpusStat(Query):
    def query_(self, report, invert_index):
        n_fp = 0
        n_skipped = 0
        n_collisions = 0
        for fingerprint, softwares in invert_index.iter_raw():
            n_fp += 1
            if invert_index.is_skipped(fingerprint):
                n_skipped += 1
            else:
                if len(softwares) > 1:
                    n_collisions += 1

        n_softwares = len(invert_index.get_softwares())
        with report.add_list() as report_list:
            report_list.append("Number of softwares: {}".format(n_softwares))
            report_list.append("Total number of fingerprints: {}".format(n_fp))
            report_list.append("Number of active fingerprints: {}"
                               "".format(n_fp - n_skipped))
            report_list.append("Number of collisions: {}".format(n_collisions))


class MostSimilar(Query):
    class AllScores(object):
        def __init__(self, software_1, software_2, scores):
            self.software_1 = software_1
            self.software_2 = software_2
            self.scores = scores

        def __iter__(self):
            for score in self.scores:
                yield score

    def __init__(self, *rankings, label=None):
        # Ordering follow the scorers[0]
        super().__init__(label)
        self.rankings = rankings
        self.ranking = ()

    def query_(self, report, invert_index):
        if len(self.rankings) == 0:
            ranking = Ranking.from_invert_index(CountSimilarity(), invert_index)
            self.rankings = (ranking,)

        header = ["Rank", "Software 1", "Software 2"] + [r.label for r in
                                                         self.rankings]

        main_ranking, other_rankings = self.rankings[0], self.rankings[1:]

        report.add_raw("First {} results".format(len(main_ranking)))

        with report.add_table(len(header), header) as table:

            for i, (main_score, software_1, software_2) in enumerate(main_ranking):

                all_scores = [main_score] + [ranking[(software_1, software_2)]
                                             for ranking in other_rankings]
                s1_name = software_1.name
                s2_name = software_2.name

                anchor = Section.create_anchor(Reference.join(s1_name, s2_name))

                row = [Reference(str(i + 1), anchor), s1_name, s2_name]

                for ranking, score in zip(self.rankings, all_scores):
                    row.append(ranking.similarity.format_score(score))
                table.append(*row)

class MatchingLocations(Query):
    def __init__(self, ranking, label=None):
        super().__init__(label)
        self.ranking = ranking

    def query_(self, report, invert_index):
        matching_graph = invert_index.derive_matching_graph()

        for _, soft_1, soft_2 in self.ranking:
            s1_name, s2_name = soft_1.name, soft_2.name
            anchor = Section.create_anchor(Reference.join(s1_name, s2_name))

            shareprints = matching_graph[(soft_1, soft_2)]
            report.add(Section("{} VS. {}".format(s1_name, s2_name), anchor))
            report.add_raw("Matching fingerprints: {}".format(len(shareprints)))
            report.add_newline()

            for fingerprint in shareprints:

                with report.add_list(str(fingerprint)) as report_list:
                    for software in (soft_1, soft_2):
                        locations = software[fingerprint]
                        for location in locations:
                            desc = "{}:{}:{}".format(location.source_file,
                                                     location.start_line,
                                                     location.start_column)
                            report_list.append(desc)

                report.add_newline()

class MatchingSnippets(Query):
    def __init__(self, ranking, pre_lines=5, post_lines=5,
                 label=None):
        super().__init__(label)
        self.ranking = ranking
        self.loc_iter = LocationIterator(pre_lines, post_lines)

    def query_(self, report, invert_index):
        matching_graph = invert_index.derive_matching_graph()

        anchors = {}

        for _, soft_1, soft_2 in self.ranking:
            s1_name, s2_name = soft_1.name, soft_2.name
            anchor = Section.create_anchor(Reference.join(s1_name, s2_name))

            report.add(Section("{} VS. {}".format(s1_name, s2_name), anchor))

            shareprints = matching_graph[(soft_1, soft_2)]

            with report.add_list("Matching fingerprints: {}".format(len(shareprints))) as li:
                for fingerprint in shareprints:
                    ref_s = Reference.join(s1_name, s2_name, str(fingerprint))
                    anchor = SubSection.create_anchor(ref_s)

                    anchors[ref_s] = anchor

                    li.append(Reference(str(fingerprint), anchor))

            report.add_newline()

            for fingerprint in shareprints:
                s_fp = str(fingerprint)
                ref_s = Reference.join(s1_name, s2_name, s_fp)
                report.add(SubSection(s_fp, anchors[ref_s]))

                for software in (soft_1, soft_2):
                    locations = software[fingerprint]
                    for location in locations:
                        desc = "{}:{}:{}".format(location.source_file,
                                                 location.start_line,
                                                 location.start_column)
                        with report.add_snippet(desc) as snippet:
                            for ln, line in self.loc_iter(location):
                                snippet.append(ln, line)

# File renderer.py
import os
from abc import ABCMeta, abstractmethod
from contextlib import contextmanager

class Renderer(object, metaclass=ABCMeta):
    @abstractmethod
    def display(self, s, **kwargs):
        pass

    def __call__(self, report):
        if report is not None:
            for block in report:
                self.display(self.dispatch(block))

    def dispatch(self, block):
        if isinstance(block, Newline):
            return self.render_newline(block)
        elif isinstance(block, Header):
            return self.render_header(block)
        elif isinstance(block, ReportList):
            return self.render_list(block)
        elif isinstance(block, Table):
            return self.render_table(block)
        elif isinstance(block, Anchor):
            return self.render_anchor(block)
        elif isinstance(block, Reference):
            return self.render_reference(block)
        elif isinstance(block, Description):
            return self.render_description(block)
        elif isinstance(block, Section):
            return self.render_section(block)
        elif isinstance(block, SubSection):
            return self.render_subsection(block)
        elif isinstance(block, Snippet):
            return self.render_snippet(block)
        elif isinstance(block, Anchorable):
            return self.render_anchorable(block)
        else:
            return self.render_raw(block)

    # -------------------------------- IN LINE --------------------------------
    @abstractmethod
    def render_newline(self, _):
        return ""

    @abstractmethod
    def render_raw(self, s):
        return ""

    @abstractmethod
    def render_anchor(self, anchor):
        return ""

    @abstractmethod
    def render_anchorable(self, anchorable):
        return ""

    @abstractmethod
    def render_reference(self, ref):
        return ""

    # --------------------------------- BLOCK ---------------------------------
    @abstractmethod
    def render_header(self, header):
        return ""

    @abstractmethod
    def render_list(self, report_list):
        return ""

    @abstractmethod
    def render_table(self, table):
        return ""

    @abstractmethod
    def render_description(self, description):
        return ""

    @abstractmethod
    def render_section(self, section):
        return ""

    @abstractmethod
    def render_subsection(self, subsection):
        return ""

    @abstractmethod
    def render_snippet(self, snippet):
        return ""


@contextmanager
def increment_width(terminal_renderer, delta):
    original_width = terminal_renderer.width
    try:
        new_width = original_width + delta
        terminal_renderer.width = new_width
        yield new_width
    finally:
        terminal_renderer.width = original_width

class TerminalRenderer(Renderer):
    def __init__(self, width=80, anchor_max_length=12):
        self.width = width
        self.anchor_max_length = anchor_max_length

    def display(self, s, **kwargs):
        print(s, **kwargs)

    def _justify(self, left, to_justify, boundaries=0):
        pad = self.width - len(left) - len(to_justify) - boundaries
        if pad < 1:
            pad = 1
        return "{}{}{}".format(left, " " * pad, to_justify)

    def _multiline(self, *lines):
        return os.linesep.join(lines)

    def render_newline(self, _):
        return os.linesep

    def render_raw(self, s):
        return s

    def render_anchor(self, anchor):
        a_str = anchor.as_hash_str()[:self.anchor_max_length-1]
        return "#{}".format(a_str)

    def render_anchorable(self, anchorable):
        a_str = self.render_anchor(anchorable.anchor)
        s = str(anchorable)
        return "{} ({})".format(s, a_str)

    def render_reference(self, ref):
        return self.render_anchorable(ref)


    def render_header(self, header):
        w = self.width - 2
        pad_len = (w - len(header)) // 2
        padding = " " * pad_len
        end_padding = " " * (w - len(header) - pad_len)
        l1 = "/{}+".format("-" * w)
        l2 = "|{}{}".format(padding, header)
        l2 = self._justify(l2, self.render_anchor(header.anchor), 2)
        l2 += " |"
        l3 = "+{}/".format("-" * w)
        return self._multiline(l1, l2, l3)

    def render_section(self, section):
        l1 = self._justify(str(section), self.render_anchor(section.anchor))
        return self._multiline(l1, "="*self.width)

    def render_subsection(self, subsection):
        l1 = self._justify(str(subsection), self.render_anchor(subsection.anchor))
        return self._multiline(l1, "-"*len(subsection))

    def render_list(self, report_list):
        ls = []
        if report_list.headline is not None:
            ls.append(self.dispatch(report_list.headline))

        for li in report_list:
            with increment_width(self, -3):
                li_str = self.dispatch(li)
            ls.append(" - {}".format(li_str))

        return self._multiline(*ls)

    def render_description(self, description):
        ls = []
        if description.headline is not None:
            ls.append(self.dispatch(description.headline))

        for k, v in description:
            with increment_width(self, -3):
                k_str = self.dispatch(k)
                with increment_width(self, -(len(k_str)+1)):
                    v_str = self.dispatch(v)

            ls.append(" - {}:{}".format(k_str, v_str))

        return self._multiline(*ls)

    def render_table(self, table):
        # Content
        column_widths = [0] * table.n_cols

        def to_content(row):
            return [self.dispatch(x) for x in row]

        def update_widths(row):
            for i, cell in enumerate(row):
                if len(cell) > column_widths[i]:
                    column_widths[i] = len(cell)

        def both(row):
            if row is None:
                return None
            new_row = to_content(row)
            update_widths(new_row)
            return new_row

        header = both(table.header)
        content = []
        for row in table:
            content.append(both(row))
        footer = both(table.footer)


        # Format
        lines = []
        column_widths = [x+2 for x in column_widths]
        def row2str(row):
            s = ""
            for w, c in zip(column_widths, row):
                s += ("| " + c.ljust(w-1))
            return s + "|"

        hline = ""
        for width in column_widths:
            hline += ("+" + "-"*width)
        hline += "+"

        lines.append(hline)
        if header:
            lines.append(row2str(header))
            lines.append(hline)
        for row in content:
            lines.append(row2str(row))
        lines.append(hline)
        if footer:
            lines.append(row2str(footer))
            lines.append(hline)
        return self._multiline(*lines)

    def render_snippet(self, snippet):
        # TODO use pygments for syntax-coloring
        lines = []
        if snippet.desc is not None:
            lines.append(snippet.desc)
        for n, line in snippet:
            lines.append("{:4}:{}".format(n, line))
        lines.append("")
        return self._multiline(*lines)

# File report.py
from hashlib import sha1
from collections import OrderedDict

class Raw(str):
    pass

class Newline(object):
    pass

class Anchor(object):
    def __init__(self, s, prefix=None):
        self.s = s
        self.prefix = prefix

    def __str__(self):
        return self.s

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__,
                                   self.s,
                                   self.prefix)

    def as_hash_str(self):
        return "{}{}".format(self.prefix if self.prefix is not None else "",
                             sha1(self.s.encode("utf-8")).hexdigest())

class Anchorable(object):
    @classmethod
    def get_prefix(cls):
        return None

    @classmethod
    def create_anchor(cls, s, anchor=None):
        if anchor is None:
            anchor = Anchor(s, prefix=cls.get_prefix())
        return anchor

    def __init__(self, s, anchor=None):
        self.s = s
        self.anchor = self.__class__.create_anchor(self.s, anchor)

    def __str__(self):
        return self.s

    def __len__(self):
        return len(self.s)

class Header(Anchorable):
    pass

class Section(Anchorable):
    @classmethod
    def get_prefix(cls):
        return "sec:"

class SubSection(Anchorable):
    @classmethod
    def get_prefix(cls):
        return "ssec:"

class Reference(object):
    @classmethod
    def join(cls, *ss):
        return "_".join(ss)

    def __init__(self, s, anchor):
        self.s = s
        self.anchor = anchor if isinstance(anchor, Anchor) else Anchor(anchor)

    def __str__(self):
        return self.s

class ReportList(object):
    def __init__(self, headline=None):
        self.headline = headline
        self.content = []

    def append(self, o):
        self.content.append(o)

    def extend(self, it):
        for x in it:
            self.append(x)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __iter__(self):
        return iter(self.content)


class Description(object):
    def __init__(self, headline=None):
        self.headline = headline
        self.content = OrderedDict()

    def append(self, k, v):
        self.content[k] = v

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __iter__(self):
        for k, v in self.content.items():
            yield k, v


class Table(object):
    def __init__(self, n_cols, header=None, footer=None):
        self.header = header
        self.rows = []
        self.footer = footer
        self.n_cols = n_cols


    def append(self, *cell_contents):
        self.rows.append(cell_contents)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __iter__(self):
        return iter(self.rows)



class Snippet(object):
    def __init__(self, desc=None):
        self.desc = desc
        self.lines = []

    def append(self, line_nb, line):
        self.lines.append((line_nb, line))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def __iter__(self):
        for line_nb, line in self.lines:
            yield line_nb, line

class Report(object):
    def __init__(self):
        self.content = []

    def __iter__(self):
        return iter(self.content)

    def add(self, x):
        self.content.append(x)

    def add_newline(self):
        self.add(Newline())

    def add_raw(self, *l):
        self.add(Raw(" ".join(str(x) for x in l)))
        return self

    def add_reference(self, readable_str, anchor_label, prefix=None):
        self.add(Reference(readable_str, Anchor(anchor_label, prefix)))

    def add_header(self, s):
        self.add(Header(s))

    def add_section(self, s):
        self.add(Section(s))

    def add_subsection(self, s):
        self.add(SubSection(s))

    def add_list(self, headline=None):
        ls = ReportList(headline)
        self.add(ls)
        return ls

    def add_description(self, headline=None):
        desc = Description(headline)
        self.add(desc)
        return desc

    def add_table(self, n_cols, header=None, footer=None):
        table = Table(n_cols, header, footer)
        self.add(table)
        return table

    def add_snippet(self, desc=None):
        snippet = Snippet(desc)
        self.add(snippet)
        return snippet

    def merge(self, other):
        self.content.extend(other.content)

# File similarity.py
from abc import ABCMeta, abstractmethod
import math
from contextlib import contextmanager

class Similarity(object, metaclass=ABCMeta):

    @property
    def label(self):
        return self.__class__.__name__

    def format_score(self, x):
        return str(x)

    @property
    def higher_more_similar(self):
        return True

    @abstractmethod
    def __call__(self, invert_index, software_1, software_2, shareprints):
        return 0.0

class Ranking(object):
    class ScoredPair(object):
        def __init__(self, score, software_1, software_2):
            self.score = score
            self.software_1 = software_1
            self.software_2 = software_2

    @classmethod
    def from_invert_index(cls, similarity, invert_index):
        ranking = cls(similarity)

        matching_graph = invert_index.derive_matching_graph()

        ls = []
        for software_1, software_2, shareprints in matching_graph:
            score = similarity(invert_index, software_1, software_2, shareprints)
            ls.append(cls.ScoredPair(score, software_1, software_2))

        ls.sort(key=lambda x: x.score,
                reverse=similarity.higher_more_similar)

        map = {}
        for i, scored_pair in enumerate(ls):
            map[(scored_pair.software_1, scored_pair.software_2)] = i

        ranking.ranking = ls
        ranking.map = map

        return ranking

    @classmethod
    def as_query(cls, similarity):
        def query(invert_index):
            return cls.from_invert_index(similarity, invert_index)
        return query

    def __init__(self, similarity):
        self.similarity = similarity
        self.ranking = None
        self.map = None
        self.max_size = None

    def __iter__(self):
        for i, scored_pair in enumerate(self.ranking):
            if self.max_size is None or i < self.max_size:
                yield scored_pair.score, scored_pair.software_1, \
                      scored_pair.software_2

    def __getitem__(self, item):
        s1, s2 = item
        i = self.map[(s1, s2)]
        return self.ranking[i].score

    def __len__(self):
        return len(self.ranking) if self.max_size is None else self.max_size

    @property
    def label(self):
        return self.similarity.label

    @contextmanager
    def top(self, k):
        max_size = self.max_size
        self.max_size = k
        try:
            yield self
        finally:
            self.max_size = max_size

class CountSimilarity(Similarity):
    @property
    def label(self):
        return "# Shareprints"

    def __call__(self, invert_index, software_1, software_2, shareprints):
        return len(shareprints)

class JaccardSimilarity(Similarity):
    @property
    def label(self):
        return "Jaccard index"

    def format_score(self, x):
        return "{:.2f}".format(x).zfill(2)

    def _count_active_fingerprints(self, invert_index, software):
        n = software.count_fingerprints()
        for fp in software.yield_fingerprints():
            if invert_index.is_skipped(fp):
                n -= 1
        return n

    def __call__(self, invert_index, software_1, software_2, shareprints):
        n_fp1 = self._count_active_fingerprints(invert_index, software_1)
        n_fp2 = self._count_active_fingerprints(invert_index, software_2)

        return float(len(shareprints)) / (n_fp1 + n_fp2 - len(shareprints))


class TfIdfSimilarity(Similarity):
    def __init__(self):
        self.tf_cache = {}
        self.idf_cache = {}
        self.norm_cache = {}

    @property
    def label(self):
        return "Cosine Tf-Idf"

    def format_score(self, x):
        return "{:.2f}".format(x).zfill(2)


    def _tf(self, invert_index, fingerprint, software):
        # Augmented Frequency (aka. double normalization 0.5) is used
        # to treat all softwares similarly, independently of the number
        # of fingerprints they contain

        max_n_fp = max(len(software[fp])
                       for fp in software.yield_fingerprints()
                       if not invert_index.is_skipped(fp))

        return .5 + .5 * len(software[fingerprint]) / float(max_n_fp)

    def _idf(self, fingerprint, invert_index):
        n_softwares = len(invert_index.get_softwares())
        n_softwares_with_fp = len(invert_index[fingerprint])
        return math.log(n_softwares / float(n_softwares_with_fp))

    def tfidf(self, invert_index, fingerprint, software):
        tf = self.tf_cache.get((fingerprint, software))
        if tf is None:
            tf = self._tf(invert_index, fingerprint, software)
            self.tf_cache[(fingerprint, software)] = tf

        idf = self.idf_cache.get(fingerprint)
        if idf is None:
            idf = self._idf(fingerprint, invert_index)
            self.idf_cache[fingerprint] = idf

        return tf * idf

    def norm(self, invert_index, software):
        x = self.norm_cache.get(software)
        if x is None:
            x = math.sqrt(sum(self.tfidf(invert_index, fingerprint, software)**2
                             for fingerprint in software.yield_fingerprints()
                              if not invert_index.is_skipped(fingerprint)))
            self.norm_cache[software] = x
        return x

    def __call__(self, invert_index, software_1, software_2, shareprints):
        # Cosine similarity
        sp = sum((self.tfidf(invert_index, fingerprint, software_1) *
                  self.tfidf(invert_index, fingerprint, software_1))
                 for fingerprint in shareprints
                 if not invert_index.is_skipped(fingerprint))

        n_1 = self.norm(invert_index, software_1)
        n_2 = self.norm(invert_index, software_2)

        # Avoid division by zero
        if n_1 == 0 or n_2 == 0:
            print("Division by zero", n_1, n_2)
            return 0.0

        return sp / (n_1 * n_2)

# File fingerprint.py
from abc import ABCMeta, abstractmethod

class Fingerprinter(object, metaclass=ABCMeta):

    def __init__(self, parser_factory):
        self.parser_factory = parser_factory

    def extract_fingerprints(self, software):
        for source_file in software:
            for x in self.extract_fingerprints_(self.parser_factory(source_file)):
                yield x

    @abstractmethod
    def extract_fingerprints_(self, token_iterator):
        raise StopIteration()

# File kgram.py
from hashlib import sha1

class Buffer(object):
    def __init__(self, capacity):
        self.circ = [None for _ in range(capacity)]
        self.top = 0

    def __iter__(self):
        size = len(self.circ)
        for i in range(size):
            o = self.circ[(self.top + i) % size]
            if o is None:
                raise StopIteration()
            yield o

    def put(self, o):
        self.circ[self.top % len(self.circ)] = o
        self.top += 1

    def is_full(self):
        return self.top >= len(self.circ)

class KGrams(object):
    @classmethod
    def default_hash_fn(cls, s):
        hashval = sha1(s.encode("utf-8"))
        hashval = hashval.hexdigest()[-4:]
        hashval = int(hashval, 16)  # using last 16 bits of sha-1 digest
        return hashval

    @classmethod
    def kgramify(cls, token_iterator, k=5):
        buffer = Buffer(k)
        for token in token_iterator:
            buffer.put(token)
            if buffer.is_full():
                tokens = list(buffer)
                yield tokens[0].location, cls([x.symbol for x in tokens])

    def __init__(self, symbols):
        self.symbols = ''.join(symbols)
        self.hash_val = self.__class__.default_hash_fn(self.symbols)

    def __len__(self):
        return len(self.symbols)

    def __hash__(self):
        return self.hash_val

    def __eq__(self, other):
        return isinstance(other, KGrams) and other.symbols == self.symbols

    def __str__(self):
        return self.symbols

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__,
                               repr(self.symbols))

# File location.py

class Location(object):
    def __init__(self, source_file, start_line, start_column):
        self.source_file = source_file
        self.start_line = start_line
        self.start_column = start_column

    def __str__(self):
        return "{}:{}:{}".format(self.source_file, self.start_line, self.start_column)

    def __repr__(self):
        return "{}({}, {}, {})".format(self.__class__.__name__,
                                       repr(self.source_file),
                                       repr(self.start_line),
                                       repr(self.start_column))

class LocationIterator(object):
    def __init__(self, pre_lines=0, post_lines=0, encoding="latin-1"):
        self.pre_lines = pre_lines
        self.post_lines = post_lines
        self.encoding = encoding

    def __call__(self, location):
        # TODO do something more efficient
        pre = max(1, location.start_line - self.pre_lines)
        post = location.start_line + self.post_lines
        with open(location.source_file, "r", encoding=self.encoding) as hdl:
            for i, line in enumerate(hdl):
                line_nb = i + 1
                if line_nb > post:
                    break
                if pre < line_nb:
                    yield line_nb, line.rstrip()

# File match.py
from collections import defaultdict

class MatchingGraph(object):
    @classmethod
    def from_invert_index(cls, invert_index):
        softwares = invert_index.get_softwares()
        graph = cls()
        for s1 in softwares:
            for fingerprint in s1.yield_fingerprints():
                matching_software = invert_index[fingerprint]
                for s2 in matching_software:
                    if s1.name < s2.name:
                        # No need to count self matches
                        # and symetry is taken care of by the graph
                        graph.add_match(s1, s2, fingerprint)

        return graph

    def __init__(self):
        self.i2s = []
        self.n2i = {}
        self.shareprints = defaultdict(set)

    def _idx(self, int_or_software):
        try:
            return int(int_or_software)
        except TypeError:
            software = int_or_software
            idx = self.n2i.get(software.name)
            if idx is None:
                idx = len(self.i2s)
                self.n2i[software.name] = idx
                self.i2s.append(software)
            return idx

    def add_match(self, s1, s2, fingerprint):
        idx1 = self._idx(s1)
        idx2 = self._idx(s2)
        idx_a, idx_b = (idx1, idx2) if idx1 < idx2 else (idx2, idx1)

        self.shareprints[(idx_a, idx_b)].add(fingerprint)

    def software_from_name(self, name):
        return self.i2s[self.n2i[name]]

    def __iter__(self):
        for (idx1, idx2), fingerprint in self.shareprints.items():
            yield self.i2s[idx1], self.i2s[idx2], fingerprint

    def __getitem__(self, item):
        idx1, idx2 = item
        idx1, idx2 = self._idx(idx1), self._idx(idx2)

        idx_a, idx_b = (idx1, idx2) if idx1 < idx2 else (idx2, idx1)

        return self.shareprints.get((idx_a, idx_b))

    def __len__(self):
        return len(self.shareprints)

# File moss.py
from collections import defaultdict

class InvertIndex(object):
    """
    `InvertIndex`
    =============
    Mapping fingerprints to softwares.

    Content is not supposed to be directly altered (use `add` and `invalidate`)
    """
    def __init__(self):
        self.hash_t = defaultdict(set)
        self.skips = set()
        self._matching_graph = None
        self._softwares = None

    def _dirty(self):
        self._matching_graph = None
        self._softwares = None

    def add(self, fingerprint, software, skip=False):
        self._dirty()
        if skip:
            self.skips.add(fingerprint)
        if fingerprint not in self.skips:
            self.hash_t[fingerprint].add(software)

    def invalidate(self, fingerprint):
        self._dirty()
        self.skips.add(fingerprint)

    def __getitem__(self, fingerprint):
        if fingerprint in self.skips:
            return frozenset()
        return self.hash_t[fingerprint]

    def __iter__(self):
        for fp, sw in self.hash_t.items():
            if fp not in self.skips:
                yield fp, sw

    def iter_raw(self):
        for fp, sw in self.hash_t.items():
            yield fp, sw

    def is_skipped(self, fingerprint):
        return fingerprint in self.skips

    def get_softwares(self):
        if self._softwares is None:
            all_soft = set()
            for softwares in self.hash_t.values():
                all_soft.update(softwares)
            self._softwares = all_soft
        return self._softwares

    def derive_matching_graph(self):
        if self._matching_graph is None:
            self._matching_graph = MatchingGraph.from_invert_index(self)
        return self._matching_graph

class Filter(object):
    def __init__(self, collision_threshold):
        self.collision_threshold = collision_threshold

    def __call__(self, invert_index):
        for fp, s in invert_index:
            if len(s) > self.collision_threshold:
                invert_index.invalidate(fp)

class MossEngine(object):
    """
    Start by adding the reference file
    """
    def __init__(self, fingerprinter, filter=None, renderer=None):
        self.fingerprinter = fingerprinter
        if filter is None:
            filter = lambda x: x
        self.filter = filter
        if renderer is None:
            renderer = TerminalRenderer()
        self.renderer = renderer
        self.invert_index = InvertIndex()

    def fingerprint(self, software):
        for location, fingerprint in self.fingerprinter.extract_fingerprints(software):
            software.add_fingerprint(fingerprint, location)

    def update_index(self, software, reference=False):
        for fp in software.fingerprints:
            self.invert_index.add(fp, software, skip=reference)

    def build_index(self, softwares, reference_software=None):
        if reference_software is not None:
            self.fingerprint(reference_software)
            self.update_index(reference_software, True)
        for software in softwares:
            self.fingerprint(software)
            self.update_index(software)
        self.filter(self.invert_index)
        return self

    def query(self, a_query):
        result = a_query(self.invert_index)
        if isinstance(result, Report):
            self.renderer(result)
        return result

# File parser.py
import os
import pygments.token
import pygments.lexers

class Token(object):
    def __init__(self, symbol, location):
        self.symbol = symbol
        self.location = location

    def __str__(self):
        return str(self.symbol)

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__,
                                       repr(self.symbol),
                                       repr(self.location))

class Parser(object):
    def __init__(self, fpath, lexer=None, encoding="latin-1"):
        self.fpath = fpath
        self.lexer = lexer
        self.encoding = encoding

    def __repr__(self):
        return "{}({}, {}, {})".format(self.__class__.__name__,
                                       repr(self.fpath),
                                       repr(self.lexer),
                                       repr(self.encoding))

    def __iter__(self):
        with open(self.fpath, "r", encoding=self.encoding) as hdl:
            text = hdl.read()
        lexer = pygments.lexers.guess_lexer_for_filename(self.fpath, text) \
            if self.lexer is None else self.lexer

        # Adapted from https://github.com/agranya99/MOSS-winnowing-seqMatcher/blob/master/cleanUP.py
        for j, line in enumerate(text.split(os.linesep)):
            line_number = j + 1
            column_number = 1
            for token_type, original_symbol in lexer.get_tokens(line):
                symbol = original_symbol
                if token_type == pygments.token.Text or token_type in pygments.token.Comment:
                    symbol = None
                elif token_type == pygments.token.Name:
                    symbol = "N"  # all variable names as 'N'
                elif token_type in pygments.token.Literal.String:
                    symbol = "S"  # all strings as 'S'
                elif token_type in pygments.token.Name.Function:
                    symbol = "F"  # user defined function names as 'F'

                if symbol is not None:
                    yield Token(symbol, Location(self.fpath, line_number,
                                                 column_number))

                column_number += len(original_symbol)

# File software.py
import glob
import os
from collections import OrderedDict
from collections import defaultdict

class Software(object):
    @classmethod
    # def list_from_globs(cls, patterns, realpath=False):
    #     tree = Tree.from_glob_pattern(patterns, realpath)
    #     return list(tree.to_software())
    
    # changes this method to accept a list of files
    def list_from_globs(cls, patterns, realpath=False):
        files = []
        for pattern in patterns:
            files.extend(glob.glob(pattern, recursive=True))
        return [cls(os.path.basename(file), [file]) for file in files]

    def __init__(self, name, files=()):
        self.name = name
        self.source_files = tuple(files)
        self.fingerprints = defaultdict(list)

    def __iter__(self):
        for source_file in self.source_files:
            yield source_file

    def add_fingerprint(self, fingerprint, location):
        self.fingerprints[fingerprint].append(location)

    def yield_fingerprints(self):
        for fp in self.fingerprints.keys():
            yield fp

    def __getitem__(self, fingerprint):
        return self.fingerprints[fingerprint]

    def count_fingerprints(self):
        return len(self.fingerprints)

    def __repr__(self):
        return "{}({}, {})".format(self.__class__.__name__,
                                   repr(self.name),
                                   repr({x for x in self}))

class Tree(object):
    @classmethod
    def from_glob_pattern(cls, patterns, realpath=False):
        tree = cls()
        for pattern in patterns:
            for file in glob.glob(pattern):
                path = os.path.expanduser(file)
                if realpath:
                    path = os.path.realpath(path)
                splits = path.split(os.sep)
                if len(splits[0]) == 0:
                    tup = (os.sep,) + tuple(splits[1:])
                else:
                    tup = tuple(splits)
                tree.insert(tup)
        return tree

    def __init__(self):
        self.children = OrderedDict()

    def insert(self, tup):
        if len(tup) == 0:
            return
        head, tail = tup[0], tup[1:]

        child = self.children.get(head)
        if child is None:
            child = Tree()
            self.children[head] = child

        child.insert(tail)

    def to_software(self):
        common = []
        children = self.children
        while len(children) < 2:
            if len(children) == 0:
                raise ValueError("No software found.")
            label, subtree = list(children.items())[0]
            common.append(label)
            children = subtree.children

        prefix = os.sep.join(common)
        for software_name, subtree in children.items():
            software_path = os.path.join(prefix, software_name)
            files = []
            for source_sub_path in subtree:
                source_path = os.path.join(software_path, source_sub_path)
                files.append(source_path)

            software = Software(software_path, files)
            yield software

    def __iter__(self):
        for label, child in self.children.items():
            if len(child.children) == 0:
                yield label
            else:
                for x in child:
                    yield os.path.join(label, x)

# File winnowing.py

class Winnower(Fingerprinter):
    def __init__(self, parser_factory, window_size, k):
        super().__init__(parser_factory)
        self.window_size = window_size
        self.k = k

    @property
    def kgramifier(self):
        # Can be overriden to change the default hash function
        return KGrams.kgramify

    def extract_fingerprints_(self, token_iterator):
        window = Buffer(self.window_size)
        selected_grams = []
        min_gram = None

        for location, kgram in self.kgramifier(token_iterator, self.k):
            window.put(kgram)
            if window.is_full():
                # Note: using built-in `min` should be much faster than
                # re-impl. it. Moreover, the window is expected to be small
                # and the cost of deriving and inverting an array should be
                # small.
                # `min` keeps the leftmost minima:
                # >> min([(1, 1), (1, 2)], key=lambda x:x[0])
                # (1, 1)
                window_min = min(list(window)[::-1], key=hash)
                if window_min is not min_gram:
                    selected_grams.append(window_min)
                    min_gram = window_min
                    yield location, window_min


# File local_moss.py

import os
from functools import partial
import sys
import pygments.lexers
import argparse

__DESC__ = "Local MOSS (measure of software similarity). "  \
           "For ease of use, consider redirecting stdout to a file. " \
           "Report the most similar softwares from a bunch looking for " \
           "matching fingerprints. A fingerprint is a kgram, and subsets of " \
           "them are selected by min-hashing over a moving window of " \
           "consecutives kgrams. See `Schleimer, S., Wilkerson, D. S., " \
           "& Aiken, A. (2003, June). Winnowing: local algorithms for " \
           "document fingerprinting. In Proceedings of the 2003 ACM " \
           "SIGMOD international conference on Management of " \
           "data (pp. 76-85)` for more details"


def select_parser_factory(lang):
    if lang is None:
        return Parser
    else:
        return partial(Parser, lexer=pygments.lexers.get_lexer_by_name(lang))

if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description=__DESC__)
    parser.add_argument("paths", nargs="*",
                        help="The paths to the software to analyze."
                             "Use path pattern for ease.") # TODO more details
    parser.add_argument("--reference", "-r", action="append",
                        help="Reference files. Files must be supplied one by one"
                             "by repeating the option."
                             "The fingerprints contained in "
                             "them will be ignored. Useful for plagiarism "
                             "detection where some code is intended to be "
                             "shared. ")
    parser.add_argument( "--language", "-l", default=None,
                         help="language of the software. If not supplied"
                              "will be guessed. See the `Short names` at "
                              "https://pygments.org/docs/lexers/")

    parser.add_argument("--window_size", "-w", default=15, type=int,
                        help="Size of the min-hashing window. The smaller,"
                             "the more fingerprints are selected. More robust "
                             "but much slower.")
    parser.add_argument("--kgram_len", "-k", default=5, type=int,
                        help="Size of the kgrams. Optimal size is "
                             "language-dependent. Longer kgrams will produce "
                             "less false-positive but will miss more "
                             "true-positives.")
    parser.add_argument("--collision_threshold", "-c", default=10, type=int,
                        help="In how many softwares a fingerprint must appear "
                             "before being discounted as too common.")
    parser.add_argument("--output_size", "-s", default="long",
                        choices=["short", "medium", "long"],
                        help="Size of the output to display")
    parser.add_argument("--top", "-t", default=15, type=int,
                        help="How many matches are reported.")
    parser.add_argument("--silent", action="store_true",
                        help="Shut up a few messages on stderr.")
    parser.add_argument("--pre_lines", default=5, type=int,
                        help="Number of lines before a fingerprint to display "
                             "when printing collisions. Ignored for "
                             "short output.")
    parser.add_argument("--post_lines", default=5, type=int,
                        help="Number of lines after a fingerprint to display "
                             "when printing collisions. Ignored for  "
                             "short output.")


    args = parser.parse_args()
    verbose = not args.silent

    metadata_query = MetaData(**{k: v for k, v in args.__dict__.items() if
                                 k != "paths"})

    parser_factory = select_parser_factory(args.language)

    fingerprinter = Winnower(parser_factory, args.window_size, args.kgram_len)
    filter = Filter(args.collision_threshold)

    moss = MossEngine(fingerprinter, filter)

    softwares = Software.list_from_globs(args.paths)

    reference = None
    if args.reference is not None and len(args.reference) > 0:
        reference = Software("Reference", args.reference)

    if verbose:
        print("Building index and matching graph...", file=sys.stderr)

    moss.build_index(softwares, reference)

    if verbose:
        print("Querying...", file=sys.stderr)
    moss.query(metadata_query)
    moss.query(SoftwareList())
    moss.query(CorpusStat())

    count_sim = moss.query(Ranking.as_query(CountSimilarity()))
    jaccard_sim = moss.query(Ranking.as_query(JaccardSimilarity()))
    tf_idf_sim = moss.query(Ranking.as_query(TfIdfSimilarity()))

    with tf_idf_sim.top(args.top):

        moss.query(MostSimilar(tf_idf_sim, jaccard_sim, count_sim))

        if args.output_size == "medium":
            moss.query(MatchingLocations(tf_idf_sim))
        elif args.output_size == "long":
            moss.query(MatchingSnippets(tf_idf_sim, pre_lines=args.pre_lines,
                                        post_lines=args.post_lines))

    if verbose:
        print()
        print("="*80)
        print("To re-run the code, use (from {})"
              "".format(os.path.realpath(os.getcwd())))
        print(" ".join(sys.argv))
        # TODO shorten the paths stuff

# Implemtation of the Locmoss class
import tempfile
class LfAdapter:
    """
    Local Fingerprinting (LF) method adapter.
    Original tool: locmoss by Jean-Michel Begon
    Repository: https://github.com/jean-michel-begon/locmoss
    """

    # Function to calculate the similarity coefficient between two pieces of code using the Locmoss algorithm.
    def get_similarity_coefficient(self, proccesed_code1, proccesed_code2):
        similarity_coefficient = 0.0
        proccesed_code1_name, proccesed_code1_content = proccesed_code1
        proccesed_code2_name, proccesed_code2_content = proccesed_code2

        # Start with provided paths (absolute when available)
        paths_to_process = [proccesed_code1_name, proccesed_code2_name]
        temp_files_created = []

        # Create temp files only when no path provided
        if proccesed_code1_name is None:
            with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".py", encoding="utf-8") as tmp1:
                tmp1.write(proccesed_code1_content)
                tmp1.flush()
                paths_to_process[0] = tmp1.name
                temp_files_created.append(tmp1.name)
        
        if proccesed_code2_name is None:
            with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".py", encoding="utf-8") as tmp2:
                tmp2.write(proccesed_code2_content)
                tmp2.flush()
                paths_to_process[1] = tmp2.name
                temp_files_created.append(tmp2.name)

        try:
            # Setting up arguments for the Locmoss algorithm
            args = {
                "paths": paths_to_process,
                "language": None,
                "collision_threshold": 10,
                # MOSS defaults (15/5) target large source files; on short
                # (tens-to-hundreds-of-token) student solutions they leave too
                # few fingerprints per file, so the Jaccard score swings wildly
                # on trivial edits. 4/3 keeps results in line with ted/csim.
                "window_size": 4,
                "kgram_len": 3,
                "top": 15,
            }
            # calculating the similarity coefficient, jaccard similarity
            parser_factory = select_parser_factory(args["language"])
            fingerprinter = Winnower(parser_factory, args["window_size"], args["kgram_len"])
            filter = Filter(args["collision_threshold"])
            moss = MossEngine(fingerprinter, filter)
            softwares = Software.list_from_globs(args["paths"])
            moss.build_index(softwares, None)
            jaccard_sim = moss.query(Ranking.as_query(JaccardSimilarity()))

            with jaccard_sim.top(args["top"]) as top_matches:
                for match in top_matches:
                    return round(match[0], 2)

        finally:
            # cleaning up temporary files
            for tmp in temp_files_created:
                try:
                    os.remove(tmp)
                except Exception:
                    pass

        return similarity_coefficient