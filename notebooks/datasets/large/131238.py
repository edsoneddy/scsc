t = int(input())
for i in range(t):
   n = int(input())
   A = []
   B = []
   while len(A)<n:
      A += [int(x) for x in input().split()]
   while len(B)<n:
      B += [int(x) for x in input().split()]
   ans = 0
   for j in range(n):
      ans += A[j] * B[j]
   print(ans)