n=int(input())
if n%4==0:
    if n//100%4==0 or n%100!=0:
        print("si")
    else:
        print("no")
else:
    print("no")
        