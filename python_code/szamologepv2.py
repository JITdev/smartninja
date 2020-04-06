
from functions import calculate

num_1 = int(input('Please enter a number: '))
num_2 = int(input('Please enter a number: '))
operand = input('Please select an operation: (+ - * /): ')

print('-' * 20)

result = calculate(num_1, num_2, operand)

print(f'Result: {result}')
print('-' * 20)
