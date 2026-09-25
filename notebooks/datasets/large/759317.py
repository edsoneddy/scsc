import sys

def main():
    palabras = set()  # Usamos un conjunto para evitar duplicados
    buffer = []  # Usamos una lista para almacenar las líneas que terminan con un guion

    for line in sys.stdin:
        line = line.rstrip()  # Eliminar espacios en blanco al final
        if line.endswith('-'):
            buffer.append(line[:-1])  # Agregar la línea sin el guion
        else:
            buffer.append(line)  # Agregar la línea completa
            texto = ''.join(buffer)  # Unir todas las líneas
            palabras.update(processar_palabras(texto))  # Procesar las palabras
            buffer = []  # Limpiar el buffer

    # Si hay contenido en el buffer después del último salto de línea
    if buffer:
        texto = ''.join(buffer)
        palabras.update(processar_palabras(texto))

    # Convertir el conjunto a una lista y ordenar
    lista_palabras = sorted(palabras)

    # Imprimir cada palabra en una línea
    print("\n".join(lista_palabras))

def processar_palabras(texto):
    # Procesar el texto y devolver las palabras encontradas
    palabras = []
    palabra = []
    for char in texto:
        if char.isalnum() or char == '-':  # Parte de una palabra
            palabra.append(char)
        else:
            if palabra:
                palabras.append(''.join(palabra).lower())  # Convertir a minúsculas y agregar
                palabra = []  # Resetear la palabra
    if palabra:  # Capturar la última palabra si existe
        palabras.append(''.join(palabra).lower())
    return palabras

if __name__ == "__main__":
    main()
