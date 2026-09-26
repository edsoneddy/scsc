T = int(input(""))

for _ in range(T):
    s = input("")
    ns = ""
    m = True

    for c in s:
        if c.isalpha():
            if m:
                ns += c.upper()
            else:
                ns += c.lower()
            m = not m
        else:
            ns += c
    print(ns)

