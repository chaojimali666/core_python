filename = 'alice.txt'

try:
	with open(filename) as file_obj:
		context = file_obj.read()
except FileNotFoundError:
	msg = "Sorry, the file "+filename+" is not found"
	print(msg)
else:
	wordlist = context.split()
	print(len(wordlist))