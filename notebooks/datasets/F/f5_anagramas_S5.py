from collections import defaultdict

# canonical key for a word: its letters in sorted order
def signature(word):
    letters = [ch for ch in word.lower() if ch.isalpha()]
    letters.sort()
    return "".join(letters)

def group_words(words):
    groups = defaultdict(list)
    for w in words:
        groups[signature(w)].append(w)
    return groups

# selection sort: bigger groups first, then alphabetical by first word
def order_groups(groups):
    ordered = [sorted(g) for g in groups.values() if len(g) > 1]
    i = 0
    while i < len(ordered):
        best = i
        for j in range(i + 1, len(ordered)):
            if len(ordered[j]) > len(ordered[best]) or (len(ordered[j]) == len(ordered[best]) and ordered[j][0] < ordered[best][0]):
                best = j
        temp = ordered[i]
        ordered[i] = ordered[best]
        ordered[best] = temp
        i = i + 1
    return ordered

def main():
    # read words until the END marker
    words = []
    line = input()
    while line != "END":
        words.append(line.strip())
        line = input()
    groups = group_words(words)
    ordered = order_groups(groups)
    if len(ordered) == 0:
        print("no anagram groups")
    else:
        for g in ordered:
            print(len(g), " ".join(g))
    singles = 0
    for g in groups.values():
        if not len(g) > 1:
            singles += 1
    label = "word" if singles == 1 else "words"
    print(singles, label, "without anagrams")

main()
