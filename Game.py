print("Please think of a number between 0 and 100!")
low = 0
high = 100
medium = (low+high)//2
state = True
while state:
    print('Is your secret number ' + str(medium))
    guess = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to in dicate I guessed correctly.")
    if guess == 'c' :
        print('Game over. Your secret number was: ' + str(medium) )
        state = False
    elif guess == 'h':
        high = medium
        medium = ( high + low ) // 2
    elif guess =='l':
        low = medium
        medium = (high + low ) // 2
    else :
        print('Sorry, I did not understand your input.')
