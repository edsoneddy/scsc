import math
def convierte(cad):
	cadn=""
	c=0
	cont=0
	while c<len(cad):
		if ord(cad[c])!=32:
			if cont%2==0:
				if ord(cad[c])<=90:
					cadn=cadn+cad[c]
				else:
					cadn=cadn+chr(ord(cad[c])-32)
				
			else:
				if ord(cad[c])<=90:
					cadn=cadn+chr(ord(cad[c])+32)
				else:
					cadn=cadn+cad[c]
			cont=cont+1

					
		else:
			cadn=cadn+' '
					
				
		
		c=c+1
	return cadn
	
n=int(input())
for i in range(n):
	cad=input()	
	print(convierte(cad))