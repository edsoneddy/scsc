num = int(input())

if (num % 4 == 0 and num % 100 != 0) or (num % 400 == 0):
    
    print("si")

else:
    
    print("no")