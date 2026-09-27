import math

# build a row of the triangle from the previous row
def next_row(prev):
    row = [1]
    for i in range(1, len(prev)):
        row.append(prev[i - 1] + prev[i])
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
    for i in range(len(row)):
        if row[i] != row[len(row) - 1 - i]:
            return False
    return True

def main():
    n = int(input())
    if not (n <= 30 and n >= 1):
        print("n out of range")
        return
    triangle = build_triangle(n)
    width = len(" ".join(str(v) for v in triangle[-1]))
    total = 0
    for row in triangle:
        print(format_row(row, width))
        total = total + sum(row)
    if 2 ** n - 1 == total:
        verdict = "sum ok"
    else:
        verdict = "sum bad"
    symmetric = True
    for row in triangle:
        if not row_is_symmetric(row):
            symmetric = False
    middle = triangle[-1][int((n - 1) / 2)]
    print("rows {} {} {}".format(n, verdict, symmetric))
    print(f"middle {middle} {math.comb(n - 1, int((n - 1) / 2)) == middle}")

main()
