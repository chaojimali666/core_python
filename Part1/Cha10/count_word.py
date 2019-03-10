def count_word(filename):
	try:
		with open(filename) as file_obj:
			context = file_obj.read()
	except FileNotFoundError:
		pass
		#msg = "Sorry, the file "+filename+" is not found"
		#print(msg)
	else:
		wordlist = context.split()
		print(len(wordlist))

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
	count_word(filename)