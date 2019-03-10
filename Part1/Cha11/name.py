from name_function import get_formatted_name
print("Enter 'q' to quit!")
while True:
	first = input("Enter your first name:\n")
	if first == 'q':
		break
	last = input("Enter your last name:\n")
	if last == 'q':
		break
	full_name = get_formatted_name(first,last)
	print('full_name is ' + full_name)