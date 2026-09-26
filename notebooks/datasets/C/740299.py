def generate_parentheses(n):
    def backtrack(current, open_count, close_count):
        if open_count == n and close_count == n:
            results.append("".join(current))
            return

        if open_count < n:
            current.append('(')
            backtrack(current, open_count + 1, close_count)
            current.pop()

        if close_count < open_count:
            current.append(')')
            backtrack(current, open_count, close_count + 1)
            current.pop()

    results = []
    backtrack([], 0, 0)
    return results

try:
    while True:
        n = int(input())
        for sequence in generate_parentheses(n):
            print(sequence)
except EOFError:
    pass
