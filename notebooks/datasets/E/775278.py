t = int(input())
for i in range(t):
  n = int(input())
  v = list(map(int, input().split()))
  u = list(map(int, input().split()))
  
  
  k = (v[i]*u[i] for i in range(len(v)))
  print(sum(k))