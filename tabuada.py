#usando .format
num = int(input('Digite o número que deseja ver a tabuada: '))
for i in range(10):
    print('{} x {} = {}'.format(num,i+1, num * (i+1)))
#usando print(f)
num = int(input('Digite o número que deseja ver a tabuada: '))
for i in range(10):
    print(f'{num} x {i+1} = {num * (i+1)}')
#normal
num = int(input('Digite o número que deseja ver a tabuada: '))
for i in range(10):
    print(str(num) + ' x ' + str(i+1) + ' = ' + str(num * (i+1)) )