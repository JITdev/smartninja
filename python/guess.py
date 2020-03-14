import random

secret = random.randint(1, 30)
guess = 0
step = 0

# for x in [0, 1, 2, 3, 4]:
#     print(f'Step: {x + 1}')
#     guess = int(input("Guess the secret number (between 1 and 30): "))
#     if guess == secret:
#         print(f"You've guessed it - congratulations! It's number {secret}.")
#         break
#     else:
#         print("Sorry, your guess is not correct... The secret number is not {guess}")


while guess != secret or step < 10:
    step += 1
    step = step + 1
    
    print(f'Step: {step}')
    
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print(f"You guessed it - congratulations! It's number {secret}.")
    else:
        print(f"Sorry, your guess is not correct... The secret number is not {guess}, it is {secret}")