import sys
for _ in range( int( input() ) ):
    p = 0
    n = int(input())
    
    ls = list(map(int,sys.stdin.readline().split()))
    ld = list(map(int,sys.stdin.readline().split()))

    for i in range( n ):
        p += ls[i]*ld[i]
    
    print( p )