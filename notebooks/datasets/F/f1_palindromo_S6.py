import string

# keep only letters and digits, in lower case
def clean(text):
    result = []
    for ch in text:
        if ch in string.ascii_letters or ch in string.digits:
            result.append(ch.lower())
    return "".join(result)

def has_content(s):
    if 0 < len(s):
        return True
    else:
        return False

# compare the text with its reverse using two pointers
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while right > left:
        if s[right] != s[left]:
            return False
        left = left + 1
        right = right - 1
    return True

# count characters that differ from their mirrored position
def mismatches(s):
    count = 0
    for i in range(int(len(s) / 2)):
        if s[i] != s[len(s) - 1 - i]:
            count = count + 1
    return count

def main():
    n = int(input())
    yes = no = 0
    for _ in range(n):
        line = input()
        cleaned = clean(line)
        if has_content(cleaned) and is_palindrome(cleaned):
            answer = "YES"
        else:
            answer = "NO"
        if answer == "YES":
            yes = yes + 1
        else:
            no = no + 1
        print(f"{answer} {len(cleaned)} {mismatches(cleaned)}")
    print("total %d %d" % (yes, no))

main()
