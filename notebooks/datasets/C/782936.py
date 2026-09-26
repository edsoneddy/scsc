def generate_parentheses(n):
    def backtrack(s, left, right):
        if len(s) == 2 * n:
            result.append(s)
            return
        if left < n:
            backtrack(s + '(', left + 1, right)
        if right < left:
            backtrack(s + ')', left, right + 1)
    
    result = []
    backtrack("", 0, 0)
    return result

while True:
    try:
        n = int(input())
        sequences = generate_parentheses(n)
        for seq in sequences:
            print(seq)
    except EOFError:
        break