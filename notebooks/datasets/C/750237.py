def generate_parentheses(n, open_count=0, close_count=0, current_sequence=""):
    if len(current_sequence) == 2 * n:
        print(current_sequence)
        return

    if open_count < n:
        generate_parentheses(n, open_count + 1, close_count, current_sequence + "(")

    if close_count < open_count:
        generate_parentheses(n, open_count, close_count + 1, current_sequence + ")")

def main():
    try:
        while True:
            n = int(input())
            generate_parentheses(n)
    except EOFError:
        pass

if __name__ == "__main__":
    main()
