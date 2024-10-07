import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    while guess!= random_number:
        guess = int(input(f'Guess a number between 1 and {x}: ' ))
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guees again. Too high.')

    print(f'Yay,congrats. You have guessed the number {random_number} correctly.')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)  # Random guess between low and high
        else:
            guess = low  # If low == high, just make the guess the low value

        feedback = input(f'Is {guess} too high (H), too low (L), or correct (C)? ').lower()

        if feedback == 'h':
            high = guess - 1  # Adjust high if the guess is too high
        elif feedback == 'l':
            low = guess + 1  # Adjust low if the guess is too low

    print(f'Yay! The computer guessed your number, {guess}, correctly!')

computer_guess(10)


computer_guess(10)
