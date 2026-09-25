import sys
import re

def procesar_texto():
    texto = sys.stdin.read()  # Leer todo el texto de entrada
    texto = texto.replace('\n', ' \n')  # Marcar saltos de línea para procesar guiones
    palabras = []
    buffer = ""  # Para manejar palabras que continúan en la siguiente línea

    for token in texto.split():
        if token.endswith('-') and token != '-':
            # Palabra con guion al final, continua en la siguiente línea
            buffer += token[:-1]
        elif buffer:
            # Continuación de la palabra
            buffer += token
            palabras.append(buffer)
            buffer = ""
        elif token != '-':
            # Palabra normal
            palabras.append(token)
    
    # Convertir a minúsculas, filtrar solo palabras válidas y eliminar duplicados
    palabras_unicas = sorted(set(re.sub(r'[^a-zA-Z\-]', '', palabra.lower()) for palabra in palabras if palabra.strip()))
    return palabras_unicas

if __name__ == "__main__":
    resultado = procesar_texto()
    print("\n".join(resultado))
