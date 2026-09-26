#!/usr/bin/env python3
"""Validación humana de pares de código, par por par, solo con teclado.

Abre cada par (File_1, File_2) de un CSV en vimdiff y pide 0/1. Guarda
progreso en un archivo .validation_progress.json junto al CSV, así se
puede pausar y retomar. El CSV final (con la columna nueva) solo se
escribe cuando TODAS las filas quedaron validadas.
"""
import argparse
import csv
import json
import os
import shutil
import subprocess
import sys
import termios
import tty


def getch():
    fd = sys.stdin.fileno()
    old = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old)
    return ch


def load_progress(path):
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            return {int(k): v for k, v in json.load(f).items()}
    return {}


def save_progress(path, progress):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(progress, f)


def show_diff(f1, f2):
    subprocess.call(["vimdiff", f1, f2])


def main():
    parser = argparse.ArgumentParser(
        description="Valida manualmente pares de código de un CSV, comparándolos con vimdiff."
    )
    parser.add_argument("csv", help="CSV de entrada (columnas File_1, File_2, ...)")
    parser.add_argument("files_dir", help="Carpeta donde están los .py referenciados en el CSV")
    parser.add_argument("-o", "--output", help="CSV de salida (default: <csv>_validated.csv)")
    parser.add_argument(
        "-c", "--column", default="Human_Label",
        help="Nombre de la columna nueva (default: Human_Label)"
    )
    parser.add_argument(
        "--show-original", action="store_true",
        help="Muestra la etiqueta original (Label/L0-L6) antes de validar. "
             "Por defecto se oculta para una revisión ciega."
    )
    args = parser.parse_args()

    if shutil.which("vimdiff") is None:
        sys.exit("No se encontró 'vimdiff' en el PATH.")

    with open(args.csv, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    total = len(rows)
    output = args.output or (os.path.splitext(args.csv)[0] + "_validated.csv")
    progress_path = os.path.splitext(args.csv)[0] + ".validation_progress.json"
    progress = load_progress(progress_path)

    order = list(range(total))
    pos = 0
    while pos < total and order[pos] in progress:
        pos += 1

    if pos == total:
        print("Todas las filas ya estaban validadas según el progreso guardado.")
    else:
        print(f"{total} pares en total, {total - len(progress)} pendientes.")
        print("Teclas: [1] similar   [0] distinto   [b] repetir diff   [u] deshacer   [q] guardar y salir\n")

        try:
            while pos < total:
                idx = order[pos]
                row = rows[idx]
                f1 = os.path.join(args.files_dir, row["File_1"])
                f2 = os.path.join(args.files_dir, row["File_2"])

                print(f"\n--- Par {idx + 1}/{total}  (validados: {len(progress)}) ---")
                print(f"  {row['File_1']}  vs  {row['File_2']}")
                if args.show_original:
                    l_flags = ",".join(row.get(f"L{n}", "") for n in range(7))
                    print(f"  [original] Label={row.get('Label')}  L0-L6={l_flags}")
                print("Abriendo vimdiff... cierra la ventana (:qa) para continuar.")
                show_diff(f1, f2)

                while True:
                    sys.stdout.write("¿Son similares? [1]=si [0]=no [b]=repetir [u]=deshacer [q]=salir: ")
                    sys.stdout.flush()
                    ch = getch()
                    print(ch)
                    if ch in ("0", "1"):
                        progress[idx] = int(ch)
                        save_progress(progress_path, progress)
                        pos += 1
                        break
                    if ch == "b":
                        show_diff(f1, f2)
                        continue
                    if ch == "u":
                        if pos == 0:
                            print("Ya estás en el primer par.")
                            continue
                        pos -= 1
                        progress.pop(order[pos], None)
                        save_progress(progress_path, progress)
                        break
                    if ch == "q":
                        save_progress(progress_path, progress)
                        print(f"\nProgreso guardado ({len(progress)}/{total}). "
                              f"Vuelve a correr el mismo comando para continuar.")
                        return
                    print("Tecla no válida.")
        except KeyboardInterrupt:
            save_progress(progress_path, progress)
            print(f"\nInterrumpido. Progreso guardado ({len(progress)}/{total}).")
            return

    if len(progress) == total:
        out_fieldnames = fieldnames + [args.column]
        with open(output, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=out_fieldnames)
            writer.writeheader()
            for idx, row in enumerate(rows):
                row[args.column] = progress[idx]
                writer.writerow(row)
        os.remove(progress_path)
        print(f"\nValidación completa. CSV generado en: {output}")


if __name__ == "__main__":
    main()
