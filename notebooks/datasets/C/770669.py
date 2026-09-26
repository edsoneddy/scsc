x=int(input())
if 1800<=x<=9999: 
    if (x%4==0 and x%100!=0) or (x%100==0 and x%400==0):
        print("si")
    else:
        print("no")