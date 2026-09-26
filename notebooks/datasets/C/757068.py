import sys
st=['0']*30
def f(k,i,j,n):
	if(j==n):
		for i in range(n*2):
			print(st[i],end='')
		print()
	else:
		if( i<n ):
			st[k] = '('
			f(k+1,i+1,j,n)
		if( i>j ):
			st[k] = ')'
			f(k+1,i,j+1,n)


for x in sys.stdin:
	n = int(x)
	f(0,0,0,n)