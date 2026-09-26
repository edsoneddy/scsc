año = int(input().strip())
if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
    print("si")
else: 
    print("no")   