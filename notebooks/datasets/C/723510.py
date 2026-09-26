def digito(n):  
    a = 0  
    while n >= 10:  
        n_str = str(n)  
        n = 1  
        for digit in n_str:  
            n *= int(digit)  
        a += 1  
    return a  

num_cases = int(input())  

for _ in range(num_cases):  
    n = int(input())  
    a = digito(n)  
    print(f"{a} pasos")