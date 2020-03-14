
num1 = int(input('Please enter a number:'))
num2 = int(input('Please enter a number:'))
operator = input('Please select an operation: (+ - * /): ')

print('-' * 20)

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 != 0:
        print(num1 / num2)
    else:
        print('Zerot division not supported.')   
else:
    print("I don't recognize this operator.")
    
print('-' * 20)
print('End!')