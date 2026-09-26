def contar_pasos(n):
    if n < 10:  
        return 0
    else:
        producto = 1
        for digito in str(n):
            producto *= int(digito)
        return 1 + contar_pasos(producto)

# Ejemplo de uso
m=int(input(""))
for i in range(m):
    n=int(input(""))
    pasos = contar_pasos(n)
    print(f"{pasos} pasos")