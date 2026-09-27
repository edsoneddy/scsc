from collections import defaultdict

# canonical key for a word: its letters in sorted order
def key_of(term):
    chars = []
    for c in term.lower():
        if c.isalpha():
            chars.append(c)
    chars.sort()
    return "".join(chars)

def bucket(terms):
    buckets = defaultdict(list)
    for t in terms:
        buckets[key_of(t)].append(t)
    return buckets

# selection sort: bigger groups first, then alphabetical by first word
def sort_groups(buckets):
    result_list = [sorted(grp) for grp in buckets.values() if len(grp) > 1]
    for a in range(len(result_list)):
        top = a
        for b in range(a + 1, len(result_list)):
            if len(result_list[b]) > len(result_list[top]) or (len(result_list[b]) == len(result_list[top]) and result_list[b][0] < result_list[top][0]):
                top = b
        result_list[a], result_list[top] = result_list[top], result_list[a]
    return result_list

def run():
    # read words until the END marker
    terms = []
    text_in = input()
    while text_in != "END":
        terms.append(text_in.strip())
        text_in = input()
    buckets = bucket(terms)
    result_list = sort_groups(buckets)
    if len(result_list) == 0:
        print("no anagram groups")
    else:
        for grp in result_list:
            print(len(grp), " ".join(grp))
    lonely = 0
    for grp in buckets.values():
        if not len(grp) > 1:
            lonely = lonely + 1
    if lonely == 1:
        noun = "word"
    else:
        noun = "words"
    print(lonely, noun, "without anagrams")

run()
