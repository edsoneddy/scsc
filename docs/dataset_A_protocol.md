# Dataset A: protocol (written before any file is generated)

This dataset replaces the first version of dataset A (see "Replacement of the
first A" at the end). The first A was small (median 13 lines / 38 csim nodes),
synthetic (`res`, `a`, `b`), had no `import`, and only 46% of its files defined
a function. The new A is meant to look like what a student hands in.

This file is committed **before** A exists so that the design cannot be
adjusted to the results. Nothing below may change after generation starts; if
something must change, the change is recorded in a dated section at the end and
the affected part of the dataset is regenerated.

## Design

* 9 original programs (`orig`), each a different problem.
* For each original, 6 variants `L1`..`L6`. **Each variant is derived from the
  original only, applying the transformations of that single Faidhi level and
  nothing else.** Variants are never derived from each other and levels are
  never accumulated (an accumulated L4 would no longer be an obfuscation of the
  original, it would be a different program that also contains L1-L3 noise).
* Positive pairs: `(orig, Lk)` for every problem and k = 1..6 -> **54 positives**,
  each labeled by construction with its level. Pairs between two variants
  (`Lj`, `Lk`) are not used: they mix levels.
* Negative pairs: every pair of two files from **different** problems (any mix of
  `orig` and variants). With 63 files that is ~1900 pairs. Two are used:
  1. the full set, for the threshold-free AUC;
  2. a random sample of 54 (to balance the classes) drawn with
     `random.Random(20260926).sample(sorted(all_negatives), 54)` over the pairs
     sorted as `(file_1, file_2)` strings with `file_1 < file_2`, for the F1 at
     the fixed threshold. The sample is not inspected before it is used.
* Labels come from the construction, not from any similarity method or model.

## Requirements for the 9 originals

Realistic student programs, Python 3, deterministic, reading from `input()` and
printing to stdout, 25-45 non-empty lines. Each one must contain:

* at least one function definition, called from the main flow;
* at least two loops (one may be nested) and at least two conditional branches;
* at least one list, dict, string or tuple manipulation with indexing or slicing;
* at least three comments;
* an `import` in at least 5 of the 9 programs;
* at least 12 distinct kinds of syntactic construct overall (assignment,
  augmented assignment, call, subscript, comparison, boolean operator, `for`,
  `while`, `if/elif/else`, `return`, arithmetic, f-string or format, ...).

The problems (different algorithms, different data types and logic):

| id | problem |
|---|---|
| p1 | exchange sort (bubble-style swaps) of a list read from input |
| p2 | primality test and prime factorization of an integer |
| p3 | word frequency count with sorted output |
| p4 | Fibonacci terms up to n and the sum of the even ones |
| p5 | row and column sums of a matrix read from input |
| p6 | decimal to binary / hexadecimal conversion building the string by hand |
| p7 | Caesar cipher with upper and lower case, shift read from input |
| p8 | balanced parentheses / brackets check with a stack |
| p9 | mean, median, mode and standard deviation of a list of numbers |

## Faidhi levels (single-level derivation)

Taxonomy of Faidhi and Robinson (1987) as used in the plagiarism-detection
literature. Each variant applies **only** the edits listed for its level, applied
broadly (at least three distinct edits when the program allows it), and must keep
the exact same input/output behavior.

| level | what may change | what must NOT change |
|---|---|---|
| L1 | comments (add, remove, reword), blank lines, indentation width, spacing around operators, line wrapping | any token of the code |
| L2 | identifier names (variables, functions, parameters) | comments, structure, statements, order |
| L3 | declarations: initial values written differently, order of the initializations, one initialization split in two or two merged (`a = 0; b = 0` <-> `a, b = 0, 0`), explicit conversions added or moved | identifiers, control flow, function boundaries |
| L4 | functions: extract a block into a new function, inline a function into its caller, split or merge functions, change parameters/returns vs. globals | statements inside blocks, conditions |
| L5 | statements replaced by equivalent ones: `for` <-> `while`, `if/elif` chains reordered or turned into a dict lookup or conditional expression, independent statements reordered, `x = x + 1` <-> `x += 1`, equivalent library call | function boundaries, the decision logic |
| L6 | decision logic and expressions: negated/De Morgan conditions, inverted branch order, different but equivalent comparison or arithmetic form, different but equivalent early-exit structure | function boundaries, declarations |

A variant that also changes something outside its level is invalid and must be
redone.

## Generation

The 9 originals and the 54 variants are written by an agent that is given only
the "Requirements", "Faidhi levels" and problem list above. It is not told what
the dataset will be evaluated with, and it must not run any similarity tool. It
may run Python to check that every variant prints exactly what its original
prints on sample inputs.

Output: `p{n}_{slug}_orig.py`, `p{n}_{slug}_L{1..6}.py` and a `MANIFEST.csv`
with columns `problem,file,level,edits` (one line per file; `edits` is a short
list of what was changed for that level).

## Evaluation (fixed in advance)

* Freeze: A is committed as generated (plus structure checks below) before any
  method is run on it.
* Structure checks allowed before freezing: file count, Python syntax, size and
  construct requirements above, and behavioral equivalence of every variant.
  No similarity score is looked at.
* Run all six methods (`ted`, `mdiff`, `lf`, `gst`, `trs`, `csim`) **once**, with
  the same threshold (0.70) as the other datasets, on the 54 positives + 54
  sampled negatives for F1/accuracy/precision/recall, and report the AUC on the
  54 positives against the full set of negatives.
* Confidence intervals: bootstrap resampling **by problem** (the 9 problems are
  the independent units), since files and pairs of one problem are not
  independent.
* Per-level recall is reported as descriptive only (9 pairs per level).
* Whatever comes out is published as it comes out.

## Known limits

* 54 + 54 pairs and 9 clusters give wide intervals (AUC roughly +-0.03): the
  dataset can show whether a method collapses on realistic code, not rank
  methods that are 0.005 apart.
* Derived variants are correct by construction but generated by a language
  model; behavioral equivalence is verified by execution, not proven.

## Replacement of the first A (2026-09-26)

The first version of A (30 hand-written files derived from a 10-line skeleton)
was discarded by the author because it was written hastily and lacks token
diversity (no imports, few functions, synthetic identifiers). It is not part of
the evaluation any more. Full disclosure: the evaluation of the six methods on
that first A had already been run (csim AUC 0.939 against 0.995+ for `lf`,
`gst` and `trs`, its worst dataset) before it was replaced, so the replacement is
not independent of that result. Its files, its pair list and that evaluation
remain in the repository history (commit `f814334` on this branch). The new A
was designed, frozen and evaluated under this protocol without looking at any
similarity score.
