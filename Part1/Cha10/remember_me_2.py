import json
filename = "username2.json"

def get_stored_name():
	try:
		with open(filename) as f_obj:
			username = json.load(f_obj)
	except FileNotFoundError:
		username = None
	return username
def get_new_name():
	username = input("What is your name:")
	print("Hello " + username +" !")
	with open(filename,'w') as f_obj:
		json.dump(username,f_obj)
def greet_user():
	username = get_stored_name()
	if username:
		print("Welcome "+username+" !")
	else:
		get_new_name()

greet_user()