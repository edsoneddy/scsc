# Dataset F: protocol (written before any file is generated)

## What this dataset is, and what it is not

F is a **stress scenario for textual and hybrid methods**: programs rewritten with many
semantically equivalent constructs at once. It was designed so that methods that compare
structure are expected to hold up and methods that compare token sequences are expected to
suffer. It is **not** a general benchmark and its results must not be presented as one; they
answer one question: in a scenario of stacked equivalent rewrites, how do structural methods
compare with textual and hybrid ones?

Fixed before this file was written: csim is frozen at release **4.1.0** (git tag `4.1.0`,
commit `0f7a6b3` of the csim repository), the six methods and adapters are those already used
for datasets A-E, the threshold is **0.70** and the similarity index is csim's default
(`legacy`). Nothing about csim, the methods or this design changes after generation starts; a
change is recorded in a dated section at the end and the affected part is regenerated.

To keep the scenario from being true by construction for csim, the equivalence catalog below
includes constructs that csim does **not** unify, and every stressed variant must use a minimum
number of them.

## Design

* 10 original programs (`orig`), each a different problem, none of them a problem of dataset A.
* Per original, 5 variants, each derived from the **original only** (never from each other):

| kind | what changes | purpose |
|---|---|---|
| `C1` | comments, blank lines, indentation width, spacing, line wrapping; not one token of code | control: every method should tie |
| `C2` | identifier names only | control: every method should tie |
| `S5` | equivalent statements (catalog S5) | stress |
| `S6` | equivalent decision logic and expressions (catalog S6) | stress |
| `SX` | a mix of both catalogs, heavily stacked | stress |

* Positive pairs: `(orig, variant)` for the 5 kinds -> **50 positives**, labeled by
  construction with their kind. Pairs between two variants are not used.
* Negative pairs: every pair of two files of **different** problems: 60 files give 1620 pairs.
  Two sets are used: all of them (AUC) and a random sample of 50 drawn with
  `random.Random(20260927).sample(sorted(all_negatives), 50)` over the pairs sorted as
  `(file_1, file_2)` strings with `file_1 < file_2` (F1 and the rest at the threshold).
* Labels come from the construction, not from any similarity method or model.

## Requirements for the 10 originals

Realistic student programs, Python 3, deterministic, reading `input()` and printing to stdout,
30-50 non-empty lines, at least three comments. Each one must contain function definitions
called from the main flow and **at least one site for each of these patterns**, so that the
catalog can be applied broadly: a comparison with `>` or `>=`; a condition with `and` / `or`;
a `not`; `x = x + ...` written in full at least once; a `for` loop over `range(...)`; a `while`
loop; an `if/else` that assigns the same variable in both branches; a loop that appends to a
list; an `import` in at least 6 of the 10 programs.

| id | problem |
|---|---|
| f1 | palindrome check after cleaning the text (letters and digits only) |
| f2 | gcd and lcm of a list of integers |
| f3 | binary search and counting occurrences in a sorted list |
| f4 | Pascal's triangle up to n rows |
| f5 | grouping words that are anagrams |
| f6 | perfect numbers up to n and digit sums |
| f7 | longest streak of days above a temperature threshold |
| f8 | bank account simulation from a list of commands (deposit, withdraw, balance) |
| f9 | roman numeral to integer and integer to roman |
| f10 | grade classification with thresholds and ranking of students |

## Equivalence catalog

Every edit of a stress variant uses one of these ids and must preserve the exact
input/output behavior. Ids marked ● and ○ are two lists; the minimum counts below are stated
per list.

**Catalog S5 (statements)**

| id | edit | list |
|---|---|---|
| s5a | `for` over `range` <-> `while` with a manual counter | ○ |
| s5b | `x = x + y` <-> `x += y` (any operator) | ● |
| s5c | `elif` chain <-> `else:` containing a nested `if` | ● |
| s5d | `if c: x = a else: x = b` <-> `x = a if c else b` | ○ |
| s5e | loop that appends to a list <-> list comprehension | ○ |
| s5f | tuple swap `a, b = b, a` <-> temporary variable | ○ |
| s5g | independent statements reordered | ○ |
| s5h | `a = b = 0` or `a, b = 0, 0` <-> separate assignments | ○ |
| s5i | `range(0, n)` <-> `range(n)`; `range(n)` <-> `range(0, n, 1)` | ○ |
| s5j | accumulating loop <-> builtin (`sum`, `max`, `min`, `any`, `all`) | ○ |
| s5k | `if c: return True else: return False` <-> `return c` | ○ |
| s5l | nested `if a: if b:` <-> `if a and b:` | ○ |

**Catalog S6 (logic and expressions)**

| id | edit | list |
|---|---|---|
| s6a | comparison written the other way round (`a > b` <-> `b < a`, `>=` <-> `<=`) | ● |
| s6b | `not (a == b)` <-> `a != b`; `not (x in y)` <-> `x not in y`; `not (a < b)` <-> `a >= b` | ● |
| s6c | De Morgan (`not (a and b)` <-> `not a or not b`) | ● |
| s6d | operands of a commutative operator or of `==` swapped | ● |
| s6e | `if not c: A else: B` <-> `if c: B else: A` | ○ |
| s6f | `len(x) == 0` <-> `not x`; `x == True` <-> `x` | ○ |
| s6g | `x ** 2` <-> `x * x` | ○ |
| s6h | equivalent arithmetic or test (`n % 2 == 0` <-> `not n % 2`, `n // 2` <-> `int(n / 2)`) | ○ |
| s6i | guard clause with early exit <-> nested `else` | ○ |
| s6j | `while True:` with `break` <-> `while cond:` | ○ |
| s6k | string building: `%`, `.format`, f-string, `+` | ○ |
| s6l | mutually exclusive `elif` conditions reordered | ○ |

**Minimums per stressed variant** (an edit counts once per distinct id, applied at as many
sites as the program has; the manifest lists the ids used):

| kind | distinct ids | from list ● | from list ○ |
|---|---|---|---|
| `S5` | at least 4, all from S5 | at least 1 | at least 2 |
| `S6` | at least 4, all from S6 | at least 2 | at least 2 |
| `SX` | at least 6, from both S5 and S6 | at least 2 | at least 3 |

Edits of one kind must not touch anything of the controls' scope (comments, identifiers are
left exactly as in the original, except what an edit forces).

## Generation

The 10 originals and the 50 variants are written by an agent given only the requirements,
the kinds, the catalog and the minimums. It is not told what the dataset will be used for or
with which methods, it must not run any similarity, plagiarism or diff tool, and it may run
Python to check that every variant prints exactly what its original prints.

Output: `f{n}_{slug}_orig.py`, `f{n}_{slug}_{C1,C2,S5,S6,SX}.py`, `MANIFEST.csv`
(`problem,file,kind,edits`; `edits` = semicolon-separated catalog ids for stress variants and
a short description for the controls) and sample inputs `tests/f{n}_in{1,2,3}.txt`.

## Checks before freezing (no similarity score is looked at)

File count, syntax, size and pattern requirements of the originals, identical output of the 6
files of each problem on 3 inputs, `C1` keeps every code token of its original, `C2` differs
from its original only in identifiers (same AST with names erased), every stress variant
differs from its original, and the manifest ids meet the minimums above and belong to the
catalog. Compliance of the edits with their catalog id is otherwise not verified
mechanically; a few variants are read by hand and any that break the rules are regenerated.

## Evaluation (fixed in advance)

* Freeze: F is committed as generated (plus the checks) before any method runs on it.
* The six methods (`ted`, `mdiff`, `lf`, `gst`, `trs`, `csim`) run **once**, threshold 0.70.
* Primary result: recall at 0.70 and mean similarity on the 30 stress positives
  (`S5`, `S6`, `SX`) per method, and the AUC of those 30 positives against all negatives with
  a bootstrap by problem (10 clusters).
* Secondary: F1, accuracy, precision, recall on the 50 + 50 sample; the controls `C1`, `C2`
  reported separately (they should tie); recall per kind, descriptive only (10 pairs each).
* Nothing is claimed about csim versus `ted` beyond describing the numbers; the question of
  the scenario is structural methods versus textual and hybrid ones.
* Whatever comes out is published as it comes out, including any result where a textual
  method does as well as a structural one.

## Known limits

* Designed to stress textual methods: a scenario, not a benchmark.
* 50 + 50 pairs and 10 clusters give wide intervals.
* Variants are generated by a language model and verified by execution, not proven.
* Mechanical compliance with the catalog is only partly verifiable.

## Deviations found in the checks before freezing (2026-09-27)

Two originals miss one of the patterns required of every original, detected by the
structure checks (no similarity score was looked at): `f2_mdc` has no `x = x + ...` written in
full and `f7_sequencia` has no condition combining `and` / `or`. Every variant of those two
problems still meets the minimums of distinct catalog ids and the per-list minimums, so the
dataset was frozen as generated instead of regenerating both problems; the variants of `f7`
use no `s6c` (De Morgan), since its original has no `and` / `or` to apply it to. Nothing else deviates: 60 files, 180 output-equivalence runs with
0 differences, `C1` keeps every code token, `C2` changes only identifiers.
