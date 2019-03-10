filename = 'holle.txt'

try:
	with open(filename) as file_obj:
		contents = file_obj
except FileNotFoundError:
	msg = "Sorry, the file "+filename+" is not found"
	print(msg)