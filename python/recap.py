# maradekos osztas
print(30 % 5)
#  az osztas egesz resze
print(30 // 5)

param1 = 'world'
param2 = 'Bob'

# valtozo beillesztese szovegbe - kulonbozo verziokkal
print('Hello %s! Hello %s!' % (param1, param2))
print('Hello {}! Hello {}!'.format('world', 'Bob'))
print('Hello {param1}! Hello {param2}!'.format(param1='world', param2='Bob'))
world = f'Hello {param1}! ' + f'Hello {param2}!'
print(world)

# szoveg darabolasa szoveg[eleje:vege]
print(world[0:5])
print(world[5:11])
print(world[-5:])
print(world[:-5])

# sorok tordelese
long_string = '#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-' + \
    '#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-'
long_string = ('#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-'
               '#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-')

# muveletek ertelmezese szovegeken
print('#-#-#-#-#-' + '#-#-#-#-#-')
print('#-' * 10)

# feltetel megadas
if False:
    print('OK')
elif True:
    print('Elif!')
else:
    pass

# az elif nelkul az elozo pelda igy nezne ki
if param1 == 'world':
    print('OK')
else:
    if param2 == 'hello':
        print('Elif!')
    else:
        print('Not OK')