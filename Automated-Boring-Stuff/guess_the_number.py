import random

number = random.randint(0,21)
counter = 0
while True:
    print('I am thinking of a number between 1 and 20.')
    print('Take a guess.')
    read_number = int(input())
    counter += 1
    if read_number == number:
        print(f'Good job! You guessed the number in {counter} guesses!')
        break
    diff = ''
    if read_number + 10 > number:
        diff = 'too high.'
    else:
        diff = 'too low.'
    print(f'Your guess is {diff}\Take a guess.')
