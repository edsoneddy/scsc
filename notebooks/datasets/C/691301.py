def generate_parentheses(n, open_count, close_count, current):
    if open_count == n and close_count == n:
        print("".join(current))
        return

    if open_count < n:
        current.append('(')
        generate_parentheses(n, open_count + 1, close_count, current)
        current.pop()

    if close_count < open_count:
        current.append(')')
        generate_parentheses(n, open_count, close_count + 1, current)
        current.pop()

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    for number in data:
        n = int(number)
        generate_parentheses(n, 0, 0, [])

if __name__ == "__main__":
    main()
