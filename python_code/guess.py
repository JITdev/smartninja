import random

end = 30
secret = random.randint(1, end)
tries = 10
guess = 0
step = 0
steps = [0, 1, 2, 3, 4]

steps[0]

for step in range(tries):
    print(f'Step: {step + 1}')
    guess = int(input("Guess the secret number (between 1 and 30): "))
    if guess == secret:
        print(f"You've guessed it - congratulations! It's number {secret}.")
        break
    else:
        print("Sorry, your guess is not correct... The secret number is not {guess}")


while guess != secret or \
        step < 10:
    step += 1
    # step = step + 1
    
    print(f'Step: {step}')
    
    guess = int(input("Guess the secret number (between 1 and 30): "))

    if guess == secret:
        print(f"You guessed it - congratulations! It's number {secret}.")
        with open("score.txt", "w") as score_file:
            score_file.write(str(step))
    else:
        print(f"Sorry, your guess is not correct... The secret number is not {guess}, it is {secret}")


# for step in range(tries):
#     print(f'Az {step+1}. probalkozas')
#     guess = int(input(f"Guess the secret number (between 1 and {end}): "))

#     if guess == secret:
#         print(f"You've guessed it - congratulations! It's number {secret}.")
#         break
#     elif step == tries-1:
#         print(f"You lost, the secret number is: {secret}")
#     elif guess > secret:
#         print("Your guess is not correct... try something smaller")
#     elif guess < secret:
#         print("Your guess is not correct... try something bigger")

with open("score.txt", "r") as score_file:
    best_score = int(score_file.read())
    print("Top score (attempts): " + str(best_score))
    