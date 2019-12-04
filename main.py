import os
import time

greeting = "Welcome brave hero! I require your assistance for a quest of sorts... This is only for those strong of will and brave of heart... before we get started, what is your name? "
y = 0
while y <= len(greeting):
    os.system("clear")
    print(greeting[:y])
    time.sleep(.03)
    y = y+1



name = input("")

if name == "Cheater" or name == "cheater":
	print("Interesting... ", name," I will be keeping a close eye on you. Are you ready to begin your journey? (Y or N) ")

elif name == "Arthur" or name == "arthur":
	print("You fancy yourself a king? We will see how worthy you are. Are you ready to begin your journey? (Y or N) ")

else:
	print ("What a funny name... ", name,"... better not be a cheater. Are you ready to begin your journey? (Y or N) ")

answer = input("")

if answer == "Y" or answer == "y":
	print("Fantastic, lets start our adventure as soon as possible! We can go to the Forest(1), Desert(2), or Mountain(3). Where should we start? (1, 2, 3) ")

	location = input("")

	# Forest 1
	if location == "1":
		print("The forest is dark, you feel a presence pulling you deeper and deeper into the forest. You find yourself lost among the tree's. Do you attempt to escape(1) or push forward unhinderd(1)?")
		print("Choose 1 or 2?")

		forest_choice1= input("")

		if forest_choice1 == "1":
			print("You begin to run, slowly moving faster and faster... your have no sense of direction in this thick forest. You see an opening up ahead and there appears to be a small cottage. What should you do?")
			print("Enter the Cottage (1)")
			print("Observe from a distance (2)")

			forest_choice2 = input("")

			if forest_choice2 == "1":
                print()
			else:
				print()

		else:
			print()

	# Desert 2
	elif location == "2":
		print()
		print()
		print()

		desert_choice1 = input("")

		if desert_choice1 == "1":
			print()
			print()
			print()

			desert_choice2 = input("")

			if desert_choice2 == "1":
				print()
			else:
				print()

		else:
			print()

	# Mountain 3
	elif location == "3":
		print()
		print()
		print()

		mountain_choice1 = input("")

		if mountain_choice1 == "1":
			print()
			print()
			print()

			mountain_choice2 = input("")

			if mountain_choice2 == "1":
				print()
			else:
				print()

		else:
			print()



else:
	print("I guess you dont want to play... too bad.")
