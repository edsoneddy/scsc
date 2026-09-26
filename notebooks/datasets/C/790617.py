p=int(input())
if p%4==0 and p%100!=0 or p%400==0:
    print("si")
else:
    print("no")