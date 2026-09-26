for _ in range(0, int(input())):
	n = int(input())
	v = input().split()
	s = 0
	for x, y in zip(v, input().split()):
		s += int(x)*int(y)
	print(s)