def generate_parentheses(n, open_count, close_count, sequence, result):
    if len(sequence) == 2 * n:
        result.append(sequence)
        return
    
    if open_count < n:
        generate_parentheses(n, open_count + 1, close_count, sequence + '(', result)
    
    if close_count < open_count:
        generate_parentheses(n, open_count, close_count + 1, sequence + ')', result)

while True:
    try:
        n = int(input())
        result = []
        generate_parentheses(n, 0, 0, "", result)
        for seq in result:
            print(seq)
    except EOFError:
        break
