import random
print('I am thinking of a number between 1 and 100.')
print('You have 7 guesses')
secret = random.randint(1,100)
for guessesTaken in range(1,8):
    print('Take a guess.')
    guess = int(input())
    if guess == secret:
        print("You got it!")
        break
    elif guess == 7:
        print("Your favorite number, but not the right answer.")
        if guess < secret:
            print('7 is too low.')
            print('You have '+str(7 - guessesTaken)+' left.')
        elif guess > secret:
            print('7 is too high.')
            print('You have '+str(7 - guessesTaken)+' left.')
    elif guess < secret:
        print("Your answer is too low.")
        print('You have '+str(7 - guessesTaken)+' left.')
    elif guess > secret:
        print('Your answer is too high.')
        print('You have '+str(7 - guessesTaken)+' left.')

if guess == secret:
    print('You got it in '+str(guessesTaken)+' guesses!')
else:
    print('You are out of guesses, the correct answer was '+str(secret))