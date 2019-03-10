import json
filename = 'username.json'
try :
	with open(filename) as f_obj:
		username = json.load(f_obj)
except FileNotFoundError:
	with open(filename,'w') as f_obj:
		username = input("Enter your name:")
		json.dump(username,f_obj)
		print("Hello" + username+"!When you come next time, you'll be rememberd!")
else:
	print("Welcome back " + username +"!")	