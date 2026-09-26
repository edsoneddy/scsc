# Generación de secuencias e paréntesis
from sys import stdin
 
 
def backtrack(actual, a, c, n):
    if len(actual) == 2 * n:
        print(actual)
        return
    if a < n:
        backtrack(actual + '(', a + 1, c, n)
    if c < a:
        backtrack(actual + ')', a, c + 1, n)
 
for linea in stdin:
    n = int(linea)
    backtrack("", 0, 0, n)
 