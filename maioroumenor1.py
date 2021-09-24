n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))

if n1 > n2:
    print(f'O maior número é o {n1}')
elif n2 > n1:
    print(f'O maior número é o {n2}')
else:
    print('Números iguais')        