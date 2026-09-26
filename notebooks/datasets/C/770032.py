N = int(input())
if N > 0:
   if N % 4 == 0 and N % 100 != 0 or N % 400 == 0:
      print("si")
   else:
      print("no")