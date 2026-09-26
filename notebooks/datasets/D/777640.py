n = int(input())
for i in range(1, n + 1):
    cad = input()
    baile = ""
    sw = 0  # mayúscula

    for j in range(len(cad)):
        if cad[j].isalpha():
            if sw == 0:
                baile += cad[j].upper()
                sw = 1
            else:
                baile += cad[j].lower()
                sw = 0
        else:
            baile += cad[j] 

    print(baile)