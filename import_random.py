import random

r = random.randint(1, 100)

while True :
	my_guess = input('Guess the number? ')
	my_guess = int(my_guess)
	if r == my_guess :
		break
	elif r < my_guess :
		print ('the number is smaller')
	elif r > my_guess :
		print ('the number is bigger')
print ('you have guess it right, its number: ', my_guess)
