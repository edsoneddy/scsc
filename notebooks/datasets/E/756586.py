import sys
import re
def diccionario2():
    lns = sys.stdin.read().splitlines()
    words = set()
    act_word = ""
    
    for l in lns:
        l = l.strip().lower()
        if l.endswith("-"):
            act_word += l[:-1]
        else:
            act_word += l
            words.update(re.findall(r'[a-z]+(?:-[a-z]+)?', act_word))
            act_word = ""
    for palabra in sorted(words):
        print(palabra)

diccionario2()
