import sys

def parentesis(n):
    def backtracking(vector, c1, c2):
        if c1 == n and c2 == n:
            combinaciones.append("".join(vector))
            return
        if c1 < n:
            vector.append('(')
            backtracking(vector, c1 + 1, c2)
            vector.pop()
        if c2 < c1:
            vector.append(')')
            backtracking(vector, c1, c2 + 1)
            vector.pop()
    combinaciones = []
    backtracking([], 0, 0)
    return combinaciones

if __name__ == '__main__':
    for linea in sys.stdin:
        linea = linea.strip()
        if linea:
            n = int(linea)
            secuencias = parentesis(n)
            for secuencia in secuencias:
                print(secuencia)