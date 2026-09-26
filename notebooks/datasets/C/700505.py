n=int(input())
if(n==1800 or n==1900):
    print("no")
else:
    if(n%4==0):
        print("si")
    else:
        print("no")