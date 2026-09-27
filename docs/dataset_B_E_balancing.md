# Balancing of datasets B-E (written after the results existed)

A and F are balanced by design (54+54 and 50+50 pairs). B-E are not: after the blind labeling
the usable pairs are B 129 positive / 101 negative, C 92 / 105, D 104 / 186, E 152 / 316.
The hypothesis of the thesis speaks of balanced datasets, so the metrics are computed on balanced
samples of B-E as well.

**This decision was taken after the scores of B-E were known.** It was not part of a protocol
written before the evaluation, and it must be reported as such.

Rule: the majority class is reduced to the size of the minority class with
`random.Random(20260927).sample(sorted(pairs), n)`, over the pairs sorted as `(File_1, File_2)`
tuples (same seed convention as dataset F). One draw, no other seed was tried to pick a result.
Afterwards the same rule was run with seeds 0..99 only as a sensitivity check of the conclusion
(range of each metric over the 100 draws is reported in the thesis).

`results/<dataset>/<method>.csv` keeps every pair; only `evaluation.ipynb` applies the sample when it reads them.
