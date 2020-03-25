print("Please choose your mood")
mood = input('a) happy b) great c) nervous :')

print('-' * 20)

if mood == 'happy' or mood == 'a':  # elagazas
    print('It is great to see you happy!')
elif mood == 'great' or mood == 'b':
    print('It is great!')
elif mood == 'nervous' or mood == 'c':
    print('Take a deep breath 3 times.')
else:
    print('I don\'t recognize this mood')

print('End!')