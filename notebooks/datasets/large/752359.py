def main():
    import sys
    i = sys.stdin.read
    d = i().splitlines()
    w = set()
    m = ""
    for l in d:
        if l.endswith('-'):
            m += l[:-1]
        else:
            m += l
            c = [word.rstrip('.,') for word in m.lower().split()]
            w.update(c)
            m = ""
    if m:
        c = [word.rstrip('.,') for word in m.lower().split()]
        w.update(c)
    s = sorted(w)
    for o in s:
        print(o)
if __name__ == "__main__":
    main()
