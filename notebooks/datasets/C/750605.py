def generar_parentesis(n, abiertos=0, cerrados=0, combinacion="", resultado=[]):
    # Caso base: cuando alcanzamos la longitud máxima de la combinación
    if abiertos == n and cerrados == n:
        resultado.append(combinacion)
        return
    
    # Agregamos un paréntesis abierto si no hemos usado todos
    if abiertos < n:
        generar_parentesis(n, abiertos + 1, cerrados, combinacion + "(", resultado)
    
    # Agregamos un paréntesis cerrado si no excede a los abiertos
    if cerrados < abiertos:
        generar_parentesis(n, abiertos, cerrados + 1, combinacion + ")", resultado)

def imprimir_secuencias_de_parentesis(n):
    resultado = []
    generar_parentesis(n, 0, 0, "", resultado)
    for secuencia in resultado:
        print(secuencia)

# Leer varios casos de prueba hasta el fin de los datos
try:
    while True:
        n = int(input().strip())
        imprimir_secuencias_de_parentesis(n)
except EOFError:
    pass
