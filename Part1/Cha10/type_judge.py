print("'q' is quit")
while  True:
	a = input("Enter your first number:\n") 
	b = input("Enter your second number:\n")
	if a == 'q' or b == 'q':
		break
	try:
		int(a)
		int(b)
	except ValueError:
		print("You must enter a number!")
	else:
		c = int(a) + int(b)
		print('The sum is {c} \n'.format(c=c))

