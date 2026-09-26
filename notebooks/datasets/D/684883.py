def convert_to_bailarina(text):
    result = ""
    upper_case = True
    for char in text:
        if char.isalpha():
            if upper_case:
                result += char.upper()
            else:
                result += char.lower()
            upper_case = not upper_case
        else:
            result += char
    return result


T = int(input())

for _ in range(T):
    text = input()
    print(convert_to_bailarina(text))
