t = int(input())
for i in range(0,t):
	cad = input()
	c = 1
	for j in cad:
		if c%2!=0 and j!=' ':
			print(j.upper(), end='')
			c = c+1
		elif c%2==0 and j!=' ':
			print(j.lower(), end='')
			c = c+1
		elif j==' ':
			print(' ', end='')
	print('\n', end='')