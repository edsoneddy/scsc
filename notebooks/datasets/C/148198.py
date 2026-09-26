def imp(n):
    def sec(izq, der, s):
        if der == n:
            print(s)
            return
        if izq < n:
            sec(izq + 1, der, s + "(")
        if der < izq:
            sec(izq, der + 1, s + ")")

    sec(0, 0, "")

if __name__ == "__main__":
    while (True):
        n = int(input())
        imp(n)