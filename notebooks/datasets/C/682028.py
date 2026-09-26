def generate_parentheses(n):
    def backtrack(S='', left=0, right=0):
        if len(S) == 2 * n:
            result.append(S)
            return
        if left < n:
            backtrack(S + '(', left + 1, right)
        if right < left:
            backtrack(S + ')', left, right + 1)

    result = []
    backtrack()
    return result

while True:
    try:
        n = int(input())
        sequences = generate_parentheses(n)
        for sequence in sorted(sequences):
            print(sequence)
    except EOFError:
        break
