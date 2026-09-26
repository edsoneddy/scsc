def solve():
    import sys
    input_data = sys.stdin.read().split()
    
    t = int(input_data[0])
    outputs = []
    
    for i in range(1, t + 1):
        n_str = input_data[i].strip()
        pasos = 0
        
        while len(n_str) > 1:
            prod = 1
            for c in n_str:
                prod *= int(c)
            n_str = str(prod)
            pasos += 1
        
        outputs.append(f"{pasos} pasos")
    
    print("\n".join(outputs))

if __name__ == '__main__':
    solve()
