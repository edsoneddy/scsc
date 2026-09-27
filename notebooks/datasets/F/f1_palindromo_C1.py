# solution handed in for the weekly exercise
import string


# NOTE: keep only letters and digits, in lower case
def clean(text):
  result = []
  for ch in text:
    if ch in string.ascii_letters or ch in string.digits:
      result.append(ch.lower())
  return "".join(result)


def has_content(s):
  if len(s) > 0:
    return True
  else:
    return False


def is_palindrome(s):
  left = 0
  right = len(s) - 1
  while left < right:
    if s[left] != s[right]:
      return False
    left = left + 1
    right = right - 1
  return True


# count characters that differ from their mirrored position (helper)
def mismatches(s):
  count = 0
  for i in range(len(s) // 2):
    if not s[i] == s[len(s) - 1 - i]:
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
    print(answer, len(cleaned), mismatches(cleaned))
  print("total", yes, no)


# start the program
main()
