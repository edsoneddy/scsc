for i in range(int(input())):
    num = int(input())
    pasos = 0
    while len(str(num)) != 1:
        str_num = str(num)
        producto = 1
        for digito in str_num:
            producto *= int(digito)
        num = producto
        pasos += 1
    print("{} pasos".format(pasos))