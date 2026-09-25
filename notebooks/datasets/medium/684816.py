def cadena_bailarina(s):
    result = []
    capitalize = True
    for char in s:
        if char.isalpha():
            if capitalize:
                result.append(char.upper())
            else:
                result.append(char.lower())
            capitalize = not capitalize
        else:
            result.append(char)
    return ''.join(result)
n = int(input())
for _ in range(n):
    text = input()
    d = cadena_bailarina(text)
    print(d)
