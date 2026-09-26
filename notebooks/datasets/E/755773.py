def procesar_entrada():
    palabras_unicas = set()
    palabra_pendiente = ""

    while True:
        try:
            linea = input().strip()
            
            if not linea and palabra_pendiente:
                palabras_unicas.add(palabra_pendiente.lower())
                palabra_pendiente = ""
                continue

            palabras_actuales = linea.split()
            
            for i, palabra in enumerate(palabras_actuales):
                palabra = palabra.rstrip('.,')

                if palabra_pendiente:
                    if palabra.endswith('-'):
                        palabra_pendiente += palabra[:-1]
                    else:
                        palabra_unida = palabra_pendiente + palabra
                        palabras_unicas.add(palabra_unida.lower())
                        palabra_pendiente = ""
                elif palabra.endswith('-'):
                    if i == len(palabras_actuales) - 1:
                        palabra_pendiente = palabra[:-1]
                    else:
                        palabras_unicas.add(palabra.lower())
                else:
                    if any(caracter.isalpha() for caracter in palabra):
                        palabras_unicas.add(palabra.lower())

        except EOFError:
            if palabra_pendiente:
                palabras_unicas.add(palabra_pendiente.lower())
            break

    palabras_finales = set()
    for palabra in palabras_unicas:
        if '-' in palabra and not palabra.endswith('-'):
            palabras_finales.add(palabra)
            palabras_finales.add(palabra.replace('-', ''))
        else:
            palabras_finales.add(palabra)

    for palabra in sorted(palabras_finales):
        print(palabra)

procesar_entrada()
