n = int(input());
for j in range(n):
    t = int(input());
    a = input().split();
    b = input().split();
    s = 0;
    for i in range(t):
        s = s + (int(a[i]) * int(b[i]));
    print(s)
