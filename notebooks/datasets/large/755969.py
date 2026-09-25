def procesar_texto(texto):
    lineas = texto.split('\n')
    
    palabra_parcial = ''
    palabras_completas = set()
    
    for linea in lineas:
        linea = ''.join(c if c.isalnum() or c in '-' else ' ' for c in linea)
        palabras = linea.split()
        
        for i, palabra in enumerate(palabras):
            if palabra_parcial:
                palabra = palabra_parcial + palabra
                palabra_parcial = ''
            
            if palabra.endswith('-'):
                if i == len(palabras) - 1:
                    palabra_parcial = palabra[:-1]
                    continue
                else:
                    palabras_completas.add(palabra.lower())
            else:
                palabras_completas.add(palabra.lower())
    
    if palabra_parcial:
        palabras_completas.add(palabra_parcial.lower())
    
    palabras_finales = sorted([p for p in palabras_completas if p])
    return palabras_finales

def main():
    # Leer entrada hasta EOF
    lineas = []
    try:
        while True:
            linea = input()
            lineas.append(linea)
    except EOFError:
        pass
    
    texto = '\n'.join(lineas)
    
    palabras = procesar_texto(texto)
    for palabra in palabras:
        print(palabra)

if __name__ == "__main__":
    main()