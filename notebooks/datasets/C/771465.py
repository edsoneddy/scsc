a = int(input())
if a%4==0:
    if a%100==0:
        if a%400==0:
            print("si")
        else:
            print("no")
    else:
        print("si")
else:
    print("no")