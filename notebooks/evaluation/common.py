"""Shared code of the per-dataset run notebooks (run_A.ipynb ... run_E.ipynb).

Each run computes the similarity score of every pair of a dataset with every
method and stores it in results/<dataset>/<method>.csv, one file per
(dataset, method), so that a slow method (ted) is computed once and never
again, and a single method can be recomputed on its own (e.g. csim after a new
release) by passing it in `force_methods`. evaluation.ipynb only reads these
files, so it can be re-run in seconds to rebuild every table and plot.

results/<dataset>/<method>.csv columns: File_1, File_2, Label, score, seconds
(`seconds` is the wall time of that single Compare call, so the time of any
subset of pairs is a plain sum).
"""
import json
import os
import platform
import time
from datetime import datetime, timezone
from importlib.metadata import version

import pandas as pd

HERE = os.path.dirname(os.path.abspath(__file__))
DATASETS_DIR = os.path.join(HERE, "..", "datasets")
VALIDATED_DIR = os.path.join(HERE, "validated_datasets")
RESULTS_DIR = os.path.join(HERE, "results")

DATASET_LETTERS = ["A", "B", "C", "D", "E"]
METHODS = ["ted", "mdiff", "lf", "gst", "trs", "csim"]


def pairs_csv(letter):
    """Pair file that is scored. A is scored on ALL its pairs (positives plus
    every cross-problem negative); the balanced sample used for the F1 is a
    subset of it (A_dataset_validated.csv) and is selected in evaluation.ipynb."""
    name = "A_full_dataset_validated.csv" if letter == "A" else f"{letter}_dataset_validated.csv"
    return os.path.join(VALIDATED_DIR, name)


def load_usable_pairs(letter):
    """Pairs whose Human_Label agrees with the original Label (see evaluation.ipynb)."""
    df = pd.read_csv(pairs_csv(letter))
    verified = df["Human_Label"].notna() & (df["Human_Label"] == df["Label"])
    return df[verified].reset_index(drop=True)


def result_path(letter, method):
    return os.path.join(RESULTS_DIR, letter, f"{method}.csv")


def _read(path):
    with open(path, "r", encoding="utf-8", errors="replace") as fh:
        return fh.read()


def run_method(letter, method, force=False):
    """Score every pair of `letter` with `method` and save it; skip if already saved."""
    path = result_path(letter, method)
    if os.path.exists(path) and not force:
        n = len(pd.read_csv(path))
        print(f"  {method:6s}: en caché ({n} pares) -> {os.path.relpath(path, HERE)}")
        return

    from scsc import Compare  # imported here: it is slow and prints adapter banners

    df = load_usable_pairs(letter)
    files_dir = os.path.join(DATASETS_DIR, letter)
    scores, seconds = [], []
    for row in df.itertuples():
        c1 = _read(os.path.join(files_dir, row.File_1))
        c2 = _read(os.path.join(files_dir, row.File_2))
        t0 = time.perf_counter()
        scores.append(Compare(c1, c2, method=method))
        seconds.append(time.perf_counter() - t0)

    out = df[["File_1", "File_2", "Label"]].copy()
    out["score"] = scores
    out["seconds"] = seconds
    os.makedirs(os.path.dirname(path), exist_ok=True)
    out.to_csv(path, index=False)

    meta_path = os.path.join(RESULTS_DIR, letter, "meta.json")
    meta = json.load(open(meta_path)) if os.path.exists(meta_path) else {}
    meta[method] = {
        "pairs": len(out),
        "seconds": round(sum(seconds), 3),
        "csim": version("csim") if method == "csim" else None,
        "python": platform.python_version(),
        "machine": platform.platform(),
        "timestamp": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    json.dump(meta, open(meta_path, "w"), indent=1)
    print(f"  {method:6s}: {sum(seconds):8.2f}s  ({len(out)} pares) -> {os.path.relpath(path, HERE)}")


def run_dataset(letter, methods=METHODS, force_methods=()):
    """Run every method on one dataset. `force_methods` recomputes only those."""
    print(f"=== Dataset {letter} ===")
    for m in methods:
        run_method(letter, m, force=m in force_methods)
