class Myclass:
	number = 0
	name = "noname"

def Main():
	me = Myclass()
	me.number = 5645
	me.name = "Muhannad"

	friend = Myclass()
	friend.number = 7
	friend.name = "Yusuf"

	empty = Myclass()

	print("Name: " + me.name + ", Favorite Number: " + str(me.number))
	print("Name: " + friend.name + ", Favorite Number: " + str(friend.number))
	print("Name: " +empty.name + ", Fav Number: " + str(empty.number))

if __name__ == '__main__':
	Main()