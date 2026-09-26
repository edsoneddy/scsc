# pair_validator

Script para validar a mano, par por par, los CSV de `notebooks/datasets/{A,B,C,D,E}`.
Por cada fila abre `vimdiff` con los dos archivos y te pide `1` (similares) o
`0` (distintos), todo con el teclado.

## Uso

```bash
python3 tools/pair_validator/validate_pairs.py <csv> <carpeta_de_archivos>
```

Ejemplo:

```bash
python3 tools/pair_validator/validate_pairs.py \
    notebooks/datasets/C/C_dataset.csv \
    notebooks/datasets/C
```

Esto abre vimdiff para cada par. Al cerrar vimdiff (`:qa`) el script pregunta:

```
¿Son similares? [1]=si [0]=no [b]=repetir [u]=deshacer [q]=salir:
```

- `1` / `0` — guarda la respuesta y pasa al siguiente par.
- `b` — vuelve a abrir vimdiff para el par actual (por si cerraste sin ver bien).
- `u` — deshace la última respuesta y te la vuelve a preguntar.
- `q` — guarda el progreso y sale. Corriendo el mismo comando después retoma donde quedaste.

El CSV de salida (`<csv>_validated.csv`, con la columna `Human_Label` agregada)
**solo se genera cuando ya validaste las 400/290/etc. filas**. Mientras tanto
el progreso vive en `<csv>.validation_progress.json`, junto al CSV original.

## Opciones

- `-o/--output`: ruta del CSV final (default: `<csv>_validated.csv`).
- `-c/--column`: nombre de la columna nueva (default: `Human_Label`).
- `--show-original`: muestra la etiqueta que puso Claude (Label, L0-L6) antes
  de que valides. Por defecto está **oculta** — para que tu validación sea
  ciega y no se contamine con la etiqueta original.
