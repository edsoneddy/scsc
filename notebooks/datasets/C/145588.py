import sys


def f(cad, A, C):
    if n == A and n == C:
        print(cad)
    if A < n:
        f(cad+'(', A+1, C)
    if A > C:
        f(cad+')', A, C+1)


if __name__ == "__main__":
    for line in sys.stdin:
        n = int(line)
        f('', 0, 0)
