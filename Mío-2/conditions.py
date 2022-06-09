x = input('Ingrese un valor: ')

try:
	x = int (x)
	if x > 0:
	    print("x is positive")
	elif x < 0:
	    print("x is negative")
	else:
	    print("x is 0")

except Exception as e:
	print ('Ocurrió el error "', e, '"')
