import datetime
import random

end = 30
secret = random.randint(1, end)
tries = 10
guess = 0
step = 0
score_list = []


for step in range(tries):
    print(f'Az {step+1}. probalkozas')
    guess = int(input(f"Guess the secret number (between 1 and {end}): "))

    # csinalunk egy dict-et a probakkal es az idobelyeggel
    score_data = {"attempts": step+1, "date": datetime.datetime.now()}
    # a dict-et hozzafuzzuk a listankhoz
    score_list.append(score_data)

    if guess == secret:
        print(f"You've guessed it - congratulations! It's number {secret}.")
        break
    elif step == tries-1:
        print(f"You lost, the secret number is: {secret}")
    elif guess > secret:
        print("Your guess is not correct... try something smaller")
    elif guess < secret:
        print("Your guess is not correct... try something bigger")


# kiirjuk a listat:
for item in score_list:
    step = item['attempts']
    date_value = item['date']
    print(f'Step: {step} at {date_value}')

# with open("score.txt", "w") as score_file:
#             score_file.write(str(score_list))

# with open("score.txt", "r") as score_file:
#     data = int(score_file.read())
#     print("Attempts:" + str(data))