# Curation of the small / medium / large datasets

The `notebooks/datasets/{small,medium,large}` datasets were rebuilt from the
solution pool in `jv-umsa-dataset/all_py` so that each one contains only files
that solve a single problem (or the minimum number of problems required),
with no exact duplicates (byte-for-byte identical content).

| Dataset | Before | After | Source problem(s) | Exact duplicates removed |
|---|---|---|---|---|
| small | 71 (accidental mix, 9 dups) | **71** | 1386 (single) | 10 |
| medium | 205 (4 mixed problems) | **200** | 1006 (single) | 96 |
| large | 401 (9 mixed problems) | **401** | 1046 + 1299 + 1118 | 73 (+2 trimmed by size) |

## Notes

- **medium ended up at 200, not 205**: no single problem in the pool has 205
  files with unique content; the largest is problem 1006, with 200.
- **large combines 3 problems**: no pair of problems reaches 401 combined
  unique files (the best pair sums to 341); the combination 1046 + 1299 + 1118
  sums to 403 unique files, of which the 2 smallest by size were trimmed to
  land exactly on 401.
- The quality filter applied was exact-duplicate removal only (same MD5
  content hash). No near-duplicate or trivial-file filtering was applied.
- The metadata CSVs (`small_dataset.csv`, `medium_dataset.csv`,
  `large_dataset.csv`, and their `*_features_dataset.csv` counterparts) were
  **not regenerated** and are now stale relative to each dataset's new
  contents. If any downstream notebook consumes them, they should be
  regenerated (see `notebooks/generate_csv_for_testing/generate_csv.ipynb`).
