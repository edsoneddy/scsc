t = int(input())
for j in range(t):
   x = input()
   sw = True
   for i in range(len(x)):
      if x[i]!=' ':
         if sw:print(x[i].upper(),end='')
         else: print(x[i].lower(),end='')
         sw = not sw
      else:print(' ',end='')
   print()