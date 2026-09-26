def sol(s,abierto,cerrado,n):
    if abierto==n and cerrado ==n:
        print(s)
    if abierto< n:
        sol(s+"(",abierto+1,cerrado,n)
 
    if abierto >cerrado :
        sol(s+")",abierto,cerrado+1,n)
 
N=10000000000
try:
    while True:
        n=int(input())
        sol("",0,0,n)
 
except EOFError:
    exit()