t = int(input().strip())
for _ in range(t):
    s = input()
    res = ""
    mayus = True  # la primera letra debe ser mayúscula
    
    for c in s:
        if c.isalpha():
            if mayus:
                res += c.upper()
            else:
                res += c.lower()
            mayus = not mayus  # alternamos
        else:
            res += c  # espacios u otros caracteres quedan igual
    
    print(res)
