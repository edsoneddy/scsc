def proceso():
    import sys
    input = sys.stdin.read
    data = input().splitlines()
    w = set()
    m = ""
    for ll in data:
        if ll.endswith('-'):
            m += ll[:-1]
        else:
            m += ll
            cw = [q.rstrip('.,') for q in m.lower().split()]
            w.update(cw)
            m = ""
    if m:
        cw = [q.rstrip('.,') for q in m.lower().split()]
        w.update(cw)
    sw = sorted(w)
    for mo in sw:
        print(mo)
if __name__ == "__main__":
    proceso()
 