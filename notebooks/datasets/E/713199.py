def process_text():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    w = set()
    m = ""

    for line in data:
        if line.endswith('-'):
            m += line[:-1]
        else:
            m += line
            cw = [word.rstrip('.,') for word in m.lower().split()]
            w.update(cw)
            m = ""

    if m:
        cw = [word.rstrip('.,') for word in m.lower().split()]
        w.update(cw)

    sw = sorted(w)

    for mo in sw:
        print(mo)


if __name__ == "__main__":
    process_text()