def my_square(x):
	return x * x

for i in range (1,11):
	print (f"The square of {i} is {my_square (i)} ")

print ("\n\n")

for i in range(1,11):
    print("{} squared is {}".format(i, my_square(i)))