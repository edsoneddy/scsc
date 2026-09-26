def generate_parentheses_with_bits(n):
    results = []
    
    def backtrack(current, open_count, close_count):

        if len(current) == 2 * n:
            results.append(current)
            return

        if open_count < n:
            backtrack(current + '(', open_count + 1, close_count)

        if close_count < open_count:
            backtrack(current + ')', open_count, close_count + 1)

    backtrack("", 0, 0)
    return results

try:
    while True:

        n = int(input().strip())

        results = generate_parentheses_with_bits(n)

        for result in results:
            print(result)
except EOFError:
    pass
