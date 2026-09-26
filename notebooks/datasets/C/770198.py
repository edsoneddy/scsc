xd=int(input())
if (xd%4==0 and xd%100!=0) or (xd%400==0):
    print("si")
else:
    print("no")