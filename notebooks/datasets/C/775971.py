x = int(input())  
if x % 400 == 0: 
    print("si")
elif x % 4 == 0 and x % 100 != 0:  
    print("si")
else:
    print("no")