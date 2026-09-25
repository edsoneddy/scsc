memo = []

def sumar(x):
    memo[memo.index(max(memo))] += x

def restar(x):
    memo[memo.index(max(memo))] -= x

dicts = {
    "S": lambda x: memo.append(int(x)),
    "A": lambda: print(max(memo)),
    "R": lambda: memo.pop(memo.index(max(memo))),
    "I": lambda x: sumar(int(x)),
    "D": lambda x: restar(int(x)),
}
while True:
    try:
        entry = tuple(input().split())

        if entry[0]=="T":
            break
        if len(entry)>1:
            dicts[entry[0]](entry[1])
        else:
            dicts[entry[0]]()         
    except Exception as e:
        print("Error")
        pass