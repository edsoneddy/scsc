t = int(input())
for _ in range(t):
    s = input()
    res = []
    upper = True
    for c in s:
        if c == " ":
            res.append(c)
            continue
        if upper:
            res.append(c.upper())
        else:
            res.append(c.lower())
        upper = not upper
    print("".join(res))
