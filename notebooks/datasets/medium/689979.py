T = int(input())
for _ in range(T):
    text = input()
    result = ""
    upper = True
    for char in text:
        if char == " ":
            result += " "
            continue
        if upper:
            result += char.upper()
            upper = False
        else:
            result += char.lower()
            upper = True
    print(result)
