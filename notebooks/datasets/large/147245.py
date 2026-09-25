def escalar(K, L):
   if len(K) != len(L):
      return 0

   return sum(i[0] * i[1] for i in zip(K, L))

n=int(input())
for i in range(n):
	escal=0
	gg=int(input())
	d=input().split()
	f=input().split()
	K=[]
	L=[]
	for y in d:
		K.append(int(y))
	for w in f:
		L.append(int(w))
	print(escalar(K,L))	