def combinar(primera, segunda, salida=None):
    if salida is None:
        salida = []
    if not primera:
        return salida + segunda
    if not segunda:
        return salida + primera
    if primera[0] <= segunda[0]:
        return combinar(primera[1:], segunda, salida + [primera[0]])
    return combinar(primera, segunda[1:], salida + [segunda[0]])


l1 = [int(x) for x in input().split()]
l2 = [int(x) for x in input().split()]
res = combinar(l1, l2)
print(" ".join(str(v) for v in res))
