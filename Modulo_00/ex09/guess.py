import random
from random import randint

print("This is an interactive guessing game!\n"
	  "You have to enter a number between 1 and 99 to find out the secret number.\n"
	  "Type exit to end the game. Good luck!")

n = randint(1,99)

guess = input("Whats your guess between 1 and 99: ")
if int(guess) == n:
	print("Congratulations, you got it on your first try!")
while (guess):
	if int(guess) not in range(1,100) or guess != "exit":
		print("Sorry, this number is out of range")
	if guess != exit:
		if int(guess) < n:
			print("Too Low!")
			guess = input("Whats your guess between 1 and 99: ")
		elif int(guess) > n:
			print("Tooo high!")
			guess = input("Whats your guess between 1 and 99: ")	

		elif int(guess) == n:
			print("Congratulations, you guessed it")
			break
	else:
		print("Goodbye!")
		break