import random
print("What is your name?")
name  = input()
print("welcome " + name + " ,well i am thinking of number between 1 to 20")
secretNumber = random.randint(1,20)

for guessesTaken in range (1,7):
    print('take a guess.')
    guess = int(input())

    if guess < secretnumber :
    print('your Guess less is too low.')
    elif guess > secretnumber :
    print('your Guess is too high')
    
else:
   break
if guess == secretnumber:
    print('good job '+ name + 'you guessd my number in' + str(guesstaken)+ 'guesses!')
else:
    print('number is was thinking of'+str(secretnumber))
