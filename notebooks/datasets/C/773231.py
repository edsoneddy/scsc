añobis = int(input())
if (añobis % 4 == 0 and añobis % 100 != 0) or (añobis % 400 == 0):
    print("si")
else:
    print("no")
