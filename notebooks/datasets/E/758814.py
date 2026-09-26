import sys
import re

def procesar_palabras(entrada):
    texto = " ".join(entrada).replace("\n", " ")
    texto = re.sub(r"-\s+", "", texto)
    palabras = re.findall(r"[a-zA-Z\-]+", texto)
    palabras = [palabra.lower() for palabra in palabras] 

    palabras_unicas = sorted(set(palabras))
    return palabras_unicas
def main():
    entrada = sys.stdin.read().strip().splitlines()
    palabras = procesar_palabras(entrada)
    for palabra in palabras:
        print(palabra)

if __name__ == "__main__":
    main()
