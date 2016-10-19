from random import randint as dice
secret_number = dice(1,9)
count = 0
name = input("Let's play a dice game, shall we? You will have 5 attempts. Input your name to confirm: ")
guest_number = 0

while (guest_number!=secret_number and count < 5):
	guest_number = input(name + " Please pick a interge number between 1 to 9 : ")
	guest_number = int (guest_number)
	count = count + 1
	if (guest_number > 9 and count < 5):
		print("It must be a number between 1 to 9")
	elif (guest_number > secret_number and count < 5):
		print("Try a smaller number, you have used "+ str(count) + " try")
	elif (guest_number < secret_number and count < 5):
		print("Try a bigger number, you have used "+ str(count) + " try")
	elif (guest_number!=secret_number and count >= 5):
		print("Sorry, the game is ended")
	else:
		print("Congradulation!You have found the correct number " + str(secret_number))
