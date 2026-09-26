f = lambda x : 'si' if (x%4 == 0 and x%100 != 0) or x%400 == 0 else 'no'
print(f(int(input())))