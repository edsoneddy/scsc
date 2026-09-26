def generate_parentheses(n):
    result = []
    
    def backtrack(current_string, open_count, close_count):
        if len(current_string) == 2 * n:
            result.append(current_string)
            return
        if open_count < n:
            backtrack(current_string + '(', open_count + 1, close_count)
        if close_count < open_count:
            backtrack(current_string + ')', open_count, close_count + 1)
    
    backtrack("", 0, 0)
    return result

def main():
    import sys
    input = sys.stdin.read
    data = input().strip().split()
    cases = [int(n) for n in data]
    
    for n in cases:
        sequences = generate_parentheses(n)
        for seq in sequences:
            print(seq)

if __name__ == "__main__":
    main()
