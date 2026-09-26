T=int(input())
for _ in range(T):
    s=input()
    r=""
    is_upper=True
    for c in s:
        if c.isalpha():
            if is_upper:
                r+=c.upper()
            else:
                r+=c.lower()
            is_upper=not is_upper
        else:
            r+=c
    print(r)
