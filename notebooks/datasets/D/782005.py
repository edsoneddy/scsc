import sys

entradas = sys.stdin.read().splitlines()
T = int(entradas[0])
for i in range(1, T + 1):
    x = entradas[i]
    bailarina = ""
    y = 0
    for j in range(len(x)):
        if x[j] == " ":
            bailarina += " "
            continue

        ascii_val = ord(x[j])
        
        if y % 2 == 0:
            if 97 <= ascii_val <= 122:
                letra = chr(ascii_val - 32)
            else:
                letra = chr(ascii_val)
        else:
            if 65 <= ascii_val <= 90:
                letra = chr(ascii_val + 32)
            else:
                letra = chr(ascii_val)
        
        bailarina += letra
        y += 1

    print(bailarina)
