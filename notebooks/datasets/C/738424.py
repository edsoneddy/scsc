def generar_combinaciones(n):
    combinaciones = []
    max_valor = 1 << (2 * n)  
    for i in range(max_valor):
        combinacion = format(i, f'0{2*n}b')  
        combinaciones.append(combinacion)
    return combinaciones
def convertir_a_parentesis(mascara):
    return ''.join('(' if bit == '0' else ')' for bit in mascara)
def es_valido(secuencia):
    balance = 0
    for char in secuencia:
        if char == '(':
            balance += 1
        else:
            balance -= 1
        if balance < 0:
            return False
    return balance == 0


def generar_secuencias_parentesis(n):
    combinaciones = generar_combinaciones(n)
    parentesis_validos = []
    
    for combinacion in combinaciones:
        secuencia = convertir_a_parentesis(combinacion)
        if es_valido(secuencia):
            parentesis_validos.append(secuencia)
    
    return parentesis_validos

while True:
    try:
        n = int(input())
        secuencias = generar_secuencias_parentesis(n)
        for secuencia in secuencias:
            print(secuencia)

    except EOFError:
        break

