def solve():
    s = input()
    n = len(s)
    sw = 1
    if (n == 1 and s[0] == ' '):
        print()
        return

    for i in range(n):
        if (s[i] != ' '):
            if (sw):
                print(s[i].upper(), end="")
            else:
                print(s[i].lower(), end="")
            sw = abs(sw - 1)
        else:
            print(end=" ")
    print()


t = int(input())
for _ in range(t):
    solve()


