def vc(x):
	x1 = x.upper()
	n = len(x)
	v = ""
	c = 1
    #print(x1)
	for i in range(n):
		x3 = ord(x[i])
		if x3 != 32:
			a = x1[i]
		    #print(a)
			if c == 0:
				a1 = a.lower()
			    #print("a1",a1)
				v = v + a1
				c = 1
			    #print(v)
			else:
				v = v + a
				c = 0
				#print(v)
		else:
			#print(x3)
			x3 = chr(x3)
			v = v + x3
	return v
n = int(input())
for i in range(n):
	x = input()
	vc1 = vc(x)
	print(vc1)