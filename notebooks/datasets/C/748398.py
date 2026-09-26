def generate_parentheses(n):
    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return
        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)
    result = []
    backtrack('', 0, 0)
    return result
try:
    while True:
        n = int(input().strip())
        sequences = generate_parentheses(n)
        for seq in sequences:
            print(seq)
except EOFError:
    pass