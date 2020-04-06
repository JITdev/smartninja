def say_hello(first_name='World', last_name=''):
    print('-' * 20)
    print(f'Hello {last_name} {first_name}!')
    print('-' * 20)

# say_hello('Roland', 'Kainrath')


def calculate(num_1, num_2, operand='+'):
    result = ''

    if operand == '+':
        result = str(num_1 + num_2)
    elif operand == '-':
        result = str(num_1 - num_2)
    elif operand == '*':
        result = str(num_1 * num_2)
    elif operand == '/':
        if num_2 != 0:
            result = str(num_1 / num_2)
        else:
            result = 'Zero division not supported.'
    else:
        result = 'I don\'t recognize this operator.'

    return result


if __name__ == "__main__":
    say_hello()
    print_this = calculate(num_1=3, num_2=0, operand='+')
    print(f'Soution: {print_this}')