b = 10 
res = 0 
for i in range(10): 
    # new statement 
    z = 10 * b 
    # foo 2 
    if i % 2 == 0: 
        a = b + 1 
    else: 
        # foo 1 
        a = b - 1 
    res = res + a 