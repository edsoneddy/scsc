for _ in range(0, int(input())):
	a = 0;
	for c in input():
		if not c.isspace():
			print(c.upper() if a%2 == 0 else c.lower(), end='')
			a += 1
		else:
			print(' ', end='')
	print()