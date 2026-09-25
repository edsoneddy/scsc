import sys, re

def main():
    partialWord, uniqueWords = '', set()
    for line in sys.stdin:
        line = line.strip()
        if line.endswith('-'):
            partialWord += line[:-1]
        else:
            partialWord += line
            uniqueWords.update(w.lower() for w in re.findall(r'[a-zA-Z\-]+', partialWord))
            partialWord = ''
    print("\n".join(sorted(uniqueWords)))

if __name__ == "__main__":
    main()
