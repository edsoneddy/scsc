def transpose(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result

r, c = map(int, input().split())
matrix = []
for _ in range(r):
    matrix.append(list(map(int, input().split())))

t = transpose(matrix)
for row in t:
    print(' '.join(map(str, row)))
