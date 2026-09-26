def is_palindrome(text):
    cleaned = []
    for ch in text:
        if ch.isalnum():
            cleaned.append(ch.lower())
    left = 0
    right = len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

line = input()
if is_palindrome(line):
    print("yes")
else:
    print("no")
