t=int(input())
for _ in range(t):
 n=input().strip()
 pasos=0
 while len(n)>1:
  p=1
  for d in n:
   p*=int(d)
  n=str(p)
  pasos+=1
 print(f"{pasos} pasos")
