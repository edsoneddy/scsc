import string

# keep only letters and digits, in lower case
def sanitize(raw):
    kept = []
    for symbol in raw:
        if symbol in string.ascii_letters or symbol in string.digits:
            kept.append(symbol.lower())
    return "".join(kept)

def not_blank(word):
    if len(word) > 0:
        return True
    else:
        return False

# compare the text with its reverse using two pointers
def reads_same(word):
    lo = 0
    hi = len(word) - 1
    while lo < hi:
        if word[lo] != word[hi]:
            return False
        lo = lo + 1
        hi = hi - 1
    return True

# count characters that differ from their mirrored position
def count_diffs(word):
    diff = 0
    for idx in range(len(word) // 2):
        if not word[idx] == word[len(word) - 1 - idx]:
            diff = diff + 1
    return diff

def run():
    cases = int(input())
    ok_count = bad_count = 0
    for _ in range(cases):
        entry = input()
        normal = sanitize(entry)
        if not_blank(normal) and reads_same(normal):
            verdict = "YES"
        else:
            verdict = "NO"
        if verdict == "YES":
            ok_count = ok_count + 1
        else:
            bad_count = bad_count + 1
        print(verdict, len(normal), count_diffs(normal))
    print("total", ok_count, bad_count)

run()
