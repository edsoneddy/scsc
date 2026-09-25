t=int(input())
for _ in range(t):
    s=input()
    r=""
    may=True
    for c in s:
        if c==" ":
            r+=" "
            continue
        r+=c.upper() if may else c.lower()
        may=not may
    print(r)