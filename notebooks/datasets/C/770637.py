n=int(input(""))
if n%100!=0 and n%4==0:
    print("si")
else:
    if n%400==0:
        print("si")
    else:
        print("no")