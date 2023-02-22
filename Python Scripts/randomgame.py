import sys
from random import randint

highest = int(sys.argv[1])
lowest = int(sys.argv[2])

answer = randint(lowest,highest)

while True:
	try:
		guess = int(input(f"Guess a random number from {lowest} to {highest}: "))
		if(guess == answer):
			print("You got it right boss!")
			break
		else:
			print("Wrong guess, try again!")
	except ValueError:
		print("Are you okay?")
		

