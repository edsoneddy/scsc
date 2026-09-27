import math

# build a row of the triangle from the previous row
def next_row(prev):
    row = [1] + [prev[i - 1] + prev[i] for i in range(1, len(prev))]
    row.append(1)
    return row

def build_triangle(n):
    triangle = []
    row = [1]
    while n > len(triangle):
        triangle.append(row)
        row = next_row(row)
    return triangle

# center a row using the width of the last row
def format_row(row, width):
    text = " ".join(str(v) for v in row)
    pad = int((width - len(text)) / 2)
    return " " * pad + text

# a row of pascal's triangle reads the same in both directions
def row_is_symmetric(row):
    i = 0
    while i < len(row):
        if row[i] != row[len(row) - 1 - i]:
            return False
        i = i + 1
    return True

def main():
    n = int(input())
    if n > 30 or n < 1:
        print("n out of range")
        return
    triangle = build_triangle(n)
    width = len(" ".join(str(v) for v in triangle[-1]))
    total = 0
    for row in triangle:
        print(format_row(row, width))
        total += sum(row)
    verdict = "sum ok" if 2 ** n - 1 == total else "sum bad"
    symmetric = True
    for row in triangle:
        if not row_is_symmetric(row):
            symmetric = False
    middle = triangle[-1][(n - 1) // 2]
    print("rows {} {} {}".format(n, verdict, symmetric))
    print("middle", middle, middle == math.comb(n - 1, (n - 1) // 2))

main()
