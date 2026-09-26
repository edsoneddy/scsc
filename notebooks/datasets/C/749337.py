def genParentesis(n):
    def bt(s='', open=0, close=0):
        if len(s) == 2 * n:
            res.append(s)
            return
        if open < n:
            bt(s + '(', open + 1, close)
        if close < open:
            bt(s + ')', open, close + 1)

    res = []
    bt()
    return res

def main():
    import sys
    for l in sys.stdin:
        n = int(l.strip())
        secu  = genParentesis(n)
        for sec in secu:
            print(sec)

if __name__ == "__main__":
    main()
