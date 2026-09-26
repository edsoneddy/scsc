def generate_parentheses_with_bits(n):
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            print("".join(current))
            return

        if open_count < n:
            current.append('(')
            backtrack(current, open_count + 1, close_count)
            current.pop()

        if close_count < open_count:
            current.append(')')
            backtrack(current, open_count, close_count + 1)
            current.pop()

    backtrack([], 0, 0)

try:
    while True:
        n = int(input().strip())
        generate_parentheses_with_bits(n)
except EOFError:
    pass
