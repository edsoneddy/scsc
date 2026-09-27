import math

# build a row of the triangle from the previous row
def make_row(above):
    line = [1]
    for k in range(1, len(above)):
        line.append(above[k - 1] + above[k])
    line.append(1)
    return line

def make_triangle(size):
    rows = []
    line = [1]
    while len(rows) < size:
        rows.append(line)
        line = make_row(line)
    return rows

# center a row using the width of the last row
def center_row(line, w):
    joined = " ".join(str(val) for val in line)
    spaces = (w - len(joined)) // 2
    return " " * spaces + joined

# a row of pascal's triangle reads the same in both directions
def mirrored(line):
    for k in range(len(line)):
        if line[k] != line[len(line) - 1 - k]:
            return False
    return True

def run():
    size = int(input())
    if size > 30 or size < 1:
        print("n out of range")
        return
    rows = make_triangle(size)
    w = len(" ".join(str(val) for val in rows[-1]))
    acc = 0
    for line in rows:
        print(center_row(line, w))
        acc = acc + sum(line)
    if acc == 2 ** size - 1:
        msg = "sum ok"
    else:
        msg = "sum bad"
    sym = True
    for line in rows:
        if not mirrored(line):
            sym = False
    center = rows[-1][(size - 1) // 2]
    print("rows", size, msg, sym)
    print("middle", center, center == math.comb(size - 1, (size - 1) // 2))

run()
