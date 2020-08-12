secret_number = 8
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guessed_number = int(input('Guess: '))
    guess_count += 1
    if guessed_number == secret_number:
        print('You Win!')
        break
    else:
        print('Wrong Guess')
else:
    print('You are out of guesses!')