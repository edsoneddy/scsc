import string

# keep only letters and digits, in lower case
def clean(text):
    result = [ch.lower() for ch in text if ch in string.ascii_letters or ch in string.digits]
    return "".join(result)

def has_content(s):
    return len(s) > 0

# compare the text with its reverse using two pointers
def is_palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

# count characters that differ from their mirrored position
def mismatches(s):
    count = 0
    i = 0
    while i < len(s) // 2:
        if not s[i] == s[len(s) - 1 - i]:
            count = count + 1
        i = i + 1
    return count

def main():
    n = int(input())
    yes = 0
    no = 0
    for _ in range(n):
        line = input()
        cleaned = clean(line)
        answer = "YES" if has_content(cleaned) and is_palindrome(cleaned) else "NO"
        if answer == "YES":
            yes = yes + 1
        else:
            no = no + 1
        print(answer, len(cleaned), mismatches(cleaned))
    print("total", yes, no)

main()
