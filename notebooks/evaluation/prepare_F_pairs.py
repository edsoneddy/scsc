"""Builds the pair files of dataset F exactly as fixed in docs/dataset_F_protocol.md.

Positives: (orig, variant) of every problem for the kinds C1, C2, S5, S6, SX (50 pairs, label 1).
Negatives: every pair of two files of different problems (label 0). Two files are written:

* F_dataset_validated.csv       50 positives + 50 negatives sampled with
                                random.Random(20260927).sample(sorted(negatives), 50)
* F_full_dataset_validated.csv  50 positives + all negatives (for the AUC)

No similarity score is used anywhere in this script.
"""
import csv
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
F_DIR = os.path.join(HERE, "..", "datasets", "F")
OUT_DIR = os.path.join(HERE, "validated_datasets")
SEED = 20260927
N_NEG_SAMPLE = 50

manifest = list(csv.DictReader(open(os.path.join(F_DIR, "MANIFEST.csv"), encoding="utf-8")))
problem_of = {r["file"]: r["problem"] for r in manifest}
files = sorted(problem_of)
header = ["File_1", "File_2", "Label", "Kind", "Notes", "Human_Label"]

positives = []
for r in manifest:
    if r["kind"] == "orig":
        continue
    orig = next(x["file"] for x in manifest if x["problem"] == r["problem"] and x["kind"] == "orig")
    positives.append([orig, r["file"], 1, r["kind"], f"orig vs {r['kind']}: {r['edits']}", 1])

negatives = sorted((a, b) for i, a in enumerate(files) for b in files[i + 1:] if problem_of[a] != problem_of[b])
sample = random.Random(SEED).sample(negatives, N_NEG_SAMPLE)
neg_row = lambda a, b: [a, b, 0, "neg", "Different problems (cross-problem pair).", 0]


def write(name, rows):
    with open(os.path.join(OUT_DIR, name), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)


write("F_dataset_validated.csv", positives + [neg_row(a, b) for a, b in sorted(sample)])
write("F_full_dataset_validated.csv", positives + [neg_row(a, b) for a, b in negatives])
print(len(positives), "positives;", len(negatives), "negatives in total;", len(sample), "sampled")
