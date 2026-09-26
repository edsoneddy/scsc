b = 10 
res = 0 
for i in range(10): 
    # foo 2 
    if i % 2 == 0: 
        a = b + 1 
    else: 
        # foo 1 
        a = b - 1 
    res = res + a 