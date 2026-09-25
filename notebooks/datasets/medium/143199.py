t=int(input())
for i in range(t):
	sw=1
	cad=input()
	cad=cad.lower()
	for i in range(len(cad)):
		if  cad[i]!=' ':
			if sw:
				print(chr(ord(cad[i])-32),end="")
				sw=0
			else:
				print(cad[i],end="")
				sw=1
		else:
			print(end=" ")
	print()