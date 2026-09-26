from sys import stdin
for linea in stdin:
    a = int(linea.strip())
    if (a%4==0 and a%100!=0) or (a%400==0):
        print("si")
    else:
        print("no")