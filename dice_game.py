from random import randint as dice

secret_number= dice(1,9)
name = input("Welcome to the dice game. What is your name? ")
guess_number = 0
loopcount = 5
while(guess_number!=secret_number and loopcount >=1):
	guess_number=input("Hello " + name+" please pick a interge number between 1 and 9 :")
	guess_number = int(guess_number)
	loopcount=(loopcount)-1
	if (guess_number == secret_number and loopcount>0):
		print ("Your number is correct. You won the game")
	elif(guess_number>secret_number and loopcount>0):
			print ("Try a lower number.Your remaining guess is "+str(loopcount))
	elif (guess_number<secret_number and loopcount>0):
			print ("Try a higher number.Your remaining guess is "+str(loopcount))
	else:
			print("Your game ended, you lose")
	

