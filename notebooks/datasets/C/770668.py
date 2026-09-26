def año_bisiesto(año):
	if año % 4 == 0:
		if año % 100 == 0:
			if año % 400 == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False
		
año = int(input())
if año_bisiesto(año):
	print(f"si")
else:
	print(f"no")