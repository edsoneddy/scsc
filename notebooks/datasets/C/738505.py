def generate_parentheses(n, open_count, close_count, current_string, result):
    if len(current_string) == 2 * n:
        result.append(current_string)
        return

    if open_count < n:
        generate_parentheses(n, open_count + 1, close_count, current_string + '(', result)

    if close_count < open_count:
        generate_parentheses(n, open_count, close_count + 1, current_string + ')', result)


def main():
    try:
        while True:
            n = int(input())
            result = []
            generate_parentheses(n, 0, 0, "", result)
            for sequence in result:
                print(sequence)
    except EOFError:
        return

if __name__ == "__main__":
    main()
