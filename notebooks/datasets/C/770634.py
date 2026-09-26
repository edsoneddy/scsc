
a=int(input())
if a%100==0:
    if (a/100)%4==0:
        print("si")
    else:
        print("no")
elif a%4==0:
    print("si")
else:
    print("no")