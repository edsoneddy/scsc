x=int(input())
for i in range (x+1):
	l=str(input())
	au=int(len(l))
	if au==0:
		print("")
	else:	
		ll=str("")
		aux=int(2)
		for auxx in range(au):
			if l[auxx]==" ":
				ll=ll+" "
			elif aux%2!=0:
				ll=ll+l[auxx].lower()
				aux=2
			else:
				ll=ll+l[auxx].upper()
				aux=1
		print(ll)