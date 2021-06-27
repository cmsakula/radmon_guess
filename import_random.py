import random

while True :
	lower_number = int( input('Enter a lower number: '))
	higher_number = int( input('Enter a higher number: '))
	if lower_number < higher_number :
		break
	else :
		print (lower_number, ' is not smaller than ', higher_number, '. Pls enter again')

r = random.randint(lower_number, higher_number)
number_of_guess = 0

while True :
	number_of_guess = number_of_guess + 1
	my_guess = input('Guess the number? ')
	my_guess = int(my_guess)
	if r == my_guess :
		break
	elif r < my_guess :
		print ('the number is smaller')
	elif r > my_guess :
		print ('the number is bigger')
print ('you have guessed ', number_of_guess, ' times. ', ' The number is ', my_guess)
