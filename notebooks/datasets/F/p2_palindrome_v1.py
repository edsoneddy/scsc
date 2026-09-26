def is_palindrome(s):
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]

text = input()
if is_palindrome(text):
    print("yes")
else:
    print("no")
