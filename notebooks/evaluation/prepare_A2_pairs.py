"""Builds the pair files of dataset A2 exactly as fixed in docs/dataset_A2_protocol.md.

Positives: (orig, Lk) of every problem, k = 1..6 (54 pairs, label 1).
Negatives: every pair of two files of different problems (label 0). Two files are written:

* A2_dataset_validated.csv       54 positives + 54 negatives sampled with
                                 random.Random(20260926).sample(sorted(negatives), 54)
                                 (for F1/accuracy/precision/recall).
* A2_full_dataset_validated.csv  54 positives + all negatives (for the AUC).

No similarity score is used anywhere in this script.
"""
import csv
import os
import random

HERE = os.path.dirname(os.path.abspath(__file__))
A2_DIR = os.path.join(HERE, "..", "datasets", "A2")
OUT_DIR = os.path.join(HERE, "validated_datasets")
SEED = 20260926
N_NEG_SAMPLE = 54

manifest = list(csv.DictReader(open(os.path.join(A2_DIR, "MANIFEST.csv"), encoding="utf-8")))
problem_of = {r["file"]: r["problem"] for r in manifest}
files = sorted(problem_of)

header = ["File_1", "File_2", "Label", "L0", "L1", "L2", "L3", "L4", "L5", "L6", "Notes", "Human_Label"]


def row(f1, f2, label, level=None, note=""):
    flags = [1 if level == k else 0 for k in range(7)]
    return [f1, f2, label, *flags, note, label]


positives = []
for r in manifest:
    if r["level"] == "orig":
        continue
    orig = next(x["file"] for x in manifest if x["problem"] == r["problem"] and x["level"] == "orig")
    positives.append(row(orig, r["file"], 1, int(r["level"]),
                         f"orig vs single-level L{r['level']} variant: {r['edits']}"))

negatives = sorted(
    (a, b) for i, a in enumerate(files) for b in files[i + 1:] if problem_of[a] != problem_of[b]
)
sample = random.Random(SEED).sample(negatives, N_NEG_SAMPLE)


def write(name, rows):
    with open(os.path.join(OUT_DIR, name), "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(header)
        w.writerows(rows)


neg_note = "Different problems (cross-problem pair)."
write("A2_dataset_validated.csv", positives + [row(a, b, 0, None, neg_note) for a, b in sorted(sample)])
write("A2_full_dataset_validated.csv", positives + [row(a, b, 0, None, neg_note) for a, b in negatives])
print(len(positives), "positives;", len(negatives), "negatives in total;", len(sample), "sampled")
