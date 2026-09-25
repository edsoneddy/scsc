import sys
import re

def process_text():

    input_text = sys.stdin.read()
    
    lines = input_text.splitlines()
    joined_text = ""
    for line in lines:
        if line.endswith("-"):
            joined_text += line[:-1]
        else:
            joined_text += line + " "

    words = re.findall(r"[a-zA-Z-]+", joined_text)

    words = [word.lower() for word in words]

    unique_words = sorted(set(words))

    for word in unique_words:
        print(word)
#======llama a la funcion
process_text()
