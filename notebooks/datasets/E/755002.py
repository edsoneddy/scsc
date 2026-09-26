import re
 
def main():
    diccionario = set()
    palabra_temporal = ""
 
    try:
        while True:
            linea_actual = input().strip()
 
            partes = re.split(r'[^a-zA-Z-]+', linea_actual)
 
            for i, segmento in enumerate(partes):
                if segmento.endswith('-') and i == len(partes) - 1:
                    palabra_temporal += segmento[:-1]
                elif segmento:
                    palabra_temporal += segmento
                    diccionario.add(palabra_temporal.lower())
                    palabra_temporal = ""
 
    except EOFError:
        pass
 
    for palabra in sorted(diccionario):
        print(palabra)
 
if __name__ == "__main__":
    main()