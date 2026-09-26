#adivina la estructura
import sys

if __name__ == '__main__':
	for line in sys.stdin:
		co = [] #cola
		pi = [] #pila
		li = [] #lista
		r = ''
		a = ''
		b = ''
		c = ''
		n = int(line)
		for i in range(n):
			s, x = list(map(int, input().rstrip().split()))
			if s == 1:
				co.append(x)
				pi.append(x)
				li.append(x)
				li.sort(reverse = True)
			else:
				r += str(x)
				a += str(co.pop(0))
				b += str(pi.pop(-1))
				c += str(li.pop(0))
		c1 = 0
		if(r == a):
			c1 += 1
		if(r == b):
			c1 += 1
		if(r == c):
			c1 += 1
		if c1 > 1 :
			print('not sure')
		else:
			if c1 == 1:
				if r == a:
					print('queue')
				else:
					if r == b:
						print('stack')
					else:
						if r == c:
							print('priority queue')
			else:
				print('impossible')
