num = int(input('Digite o número que deseja ver a tabuada: '))
for i in range(10):
    print(str(num) + ' x ' + str(i+1) + ' = ' + str(num * (i+1)) )