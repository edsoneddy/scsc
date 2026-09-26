#!/usr/bin/env python3
"""Prepara los 5 CSV de datasets/{A..E} para el análisis de evaluation.ipynb.

Toma cada `<X>_dataset.csv` de notebooks/datasets/<X>/ y escribe una copia en
validated_datasets/<X>_dataset_validated.csv con una columna `Human_Label`
agregada.

Uso normal (después de correr tools/pair_validator sobre los 5 CSV reales):
    python3 prepare_validated_datasets.py --from-validated

Modo placeholder (mientras no se ha validado a mano todavía, para poder
construir y probar las notebooks de una vez): copia el CSV original y pone
Human_Label = Label en todas las filas, es decir simula que un humano
revisó y confirmó el 100% de los pares. evaluation.ipynb filtra las filas
donde Human_Label == Label antes de calcular cualquier métrica, así que
correrlo así usa TODAS las filas; en cuanto reemplaces estos CSV por los
que sí pasaron por tools/pair_validator, las filas donde el humano no
esté de acuerdo con la etiqueta original quedan excluidas automáticamente.
"""
import argparse
import csv
import os

DATASETS = ["A", "B", "C", "D", "E"]
HERE = os.path.dirname(os.path.abspath(__file__))
DATASETS_DIR = os.path.join(HERE, "..", "datasets")
OUT_DIR = os.path.join(HERE, "validated_datasets")


def placeholder_copy(src_csv, dst_csv):
    with open(src_csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames) + ["Human_Label"]
        rows = list(reader)

    for row in rows:
        row["Human_Label"] = row["Label"]

    with open(dst_csv, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def use_already_validated(src_csv, dst_csv, human_csv):
    """Copia human_csv (salida real de tools/pair_validator) a dst_csv tal cual."""
    with open(human_csv, newline="", encoding="utf-8") as f:
        content = f.read()
    with open(dst_csv, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--from-validated", action="store_true",
        help="Usa notebooks/datasets/<X>/<X>_dataset_validated.csv (salida real "
             "de tools/pair_validator) en vez de generar un placeholder."
    )
    args = parser.parse_args()

    os.makedirs(OUT_DIR, exist_ok=True)

    for ds in DATASETS:
        src = os.path.join(DATASETS_DIR, ds, f"{ds}_dataset.csv")
        dst = os.path.join(OUT_DIR, f"{ds}_dataset_validated.csv")

        if args.from_validated:
            human = os.path.join(DATASETS_DIR, ds, f"{ds}_dataset_validated.csv")
            if not os.path.exists(human):
                raise SystemExit(
                    f"No existe {human}. Corre tools/pair_validator sobre "
                    f"{src} primero, o quita --from-validated para usar el placeholder."
                )
            use_already_validated(src, dst, human)
            print(f"{ds}: copiado desde validación real -> {dst}")
        else:
            placeholder_copy(src, dst)
            print(f"{ds}: placeholder (Human_Label = Label) -> {dst}")


if __name__ == "__main__":
    main()
