T = int(input())
 
for _ in range(T):
    text = input()
    result = ""
    upper = True
    
    for char in text:
        if char.isalpha():
            if upper:
                result += char.upper()
            else:
                result += char.lower()
            upper = not upper
        else:
            result += char
    
    print(result)