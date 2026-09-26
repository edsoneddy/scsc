año = int(input())
if año % 400 == 0:
    print("si")
elif año % 100 == 0:
    print("no")
elif año % 4 == 0:
    print("si")
else:
    print("no")
