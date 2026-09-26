def generate_parentheses(n):
    stack = []
    result = []

    def backtrack(left, right):
        if left == 0 and right == 0:
            result.append(''.join(stack))
            return

        if left > 0:
            stack.append('(')
            backtrack(left - 1, right)
            stack.pop()

        if right > left:
            stack.append(')')
            backtrack(left, right - 1)
            stack.pop()

    backtrack(n, n)
    return result

while True:
    try:
        n = int(input().strip())
        if n <= 0 or n > 10:
            raise ValueError("Input must be an integer between 1 and 10 inclusive.")
        for seq in generate_parentheses(n):
            print(seq)
    except ValueError as ve:
        print(ve)
    except EOFError:
        break
