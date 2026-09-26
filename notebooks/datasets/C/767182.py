def contar_pasos(n: int) -> int:
    if n < 10:
        return 0
    pasos = 0
    while n >= 10:
        nuevo_n = 1
        for digito in str(n):
            nuevo_n *= int(digito)
        n = nuevo_n
        pasos += 1
    return pasos

num_casos = int(input())
for _ in range(num_casos):
  _input = int(input())
  print(f"{contar_pasos(_input)} pasos")