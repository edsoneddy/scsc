def generate_sequences(open, close, sequence, n):
    if len(sequence) == 2 * n:
        print(sequence)
        return
    
    if open < n:
        generate_sequences(open + 1, close, sequence + "(", n)
    
    if close < open:
        generate_sequences(open, close + 1, sequence + ")", n)

def main():
    try:
        while True:
            n = int(input())
            generate_sequences(0, 0, "", n)
    except EOFError:
        pass  # Termina cuando no hay más entradas

if __name__ == "__main__":
    main()

