import sys
lineas = sys.stdin.readlines()
for linea in lineas:
    n = int(linea.strip())

    stack = []

    def generate_parentesis(stack, open, close, n):
        if open == close == n:
            print(''.join(stack))
        if open < n:
            stack.append("(")
            generate_parentesis(stack, open+1, close, n)
            stack.pop()
        if close < open:
            stack.append(")")
            generate_parentesis(stack, open, close+1, n)
            stack.pop()
        
    generate_parentesis(stack, 0, 0, n)
