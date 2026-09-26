t = int(input())
for _ in range(t):
    c = input()
    r = ""
    m = 0
    for i in c:
        if 'a' <= i.lower() <= 'z':
            if m == 0:
                r = r + i.upper()
            else:
                r = r + i.lower()
            if m == 0:
                m = 1
            else:
                m = 0
        else:
            r = r + i
    print(r)