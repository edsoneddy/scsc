m = [] 
def s(x):
    m[m.index(max(m))] += x
def r(x):
    m[m.index(max(m))] -= x
d = {
    "S": lambda x: m.append(int(x)),
    "A": lambda: print(max(m)),
    "R": lambda: m.pop(m.index(max(m))),
    "I": lambda x: s(int(x)),
    "D": lambda x: r(int(x)),
}
while True:
    try:
        n = tuple(input().split())
        if n[0] == "T":
            break
        if len(n) > 1:
            d[n[0]](n[1])
        else:
            d[n[0]]()         
    except Exception as e:
        print("Error")
        pass