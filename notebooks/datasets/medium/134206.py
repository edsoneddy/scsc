n=int(input())
for i in range(n+1):
	t=input()
	p=t.upper()
	s=t.lower()
	l=len(t)
	c=1
	if len(t)>0:
		nt=p[0]
		for j in range(1,l+1):
			if c<l:
				if t[j] != ' ':
					if c%2==0:
						nt=nt+p[j:j+1]
					else:
						nt=nt+s[j:j+1]
				else:
					nt=nt+' '
					c+=1
					l=l+1
			c=c+1
		print(nt)