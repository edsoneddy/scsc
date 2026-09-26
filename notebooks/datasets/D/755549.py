t=int(input())
for _ in range(t):
 c=input()
 r=""
 m=True
 for i in c:
  if i.isalpha():
   r+=i.upper() if m else i.lower()
   m=not m
  else:
   r+=i
 print(r)
