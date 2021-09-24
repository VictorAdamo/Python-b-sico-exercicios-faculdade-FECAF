print('CALCULADORA SIMPLES DE 2 VALORES.')

def Linhas():
    print('=' * 15)

while True:
    escolha = int(input('1 = Adição, 2 = Subtração, 3 = Multiplicação, 4 = Divisão (Escolha): '))
    Linhas()
    if escolha == 1:
        x1 = float(input('Primeiro número: '))
        z1 = float(input('Segundo número: '))
        op1 = x1 + z1
        Linhas()
        print(f'{x1} + {z1} = {op1}.')
        Linhas()
    elif escolha == 2:
        x2 = float(input('Primeiro número: '))
        z2 = float(input('Segundo número: '))
        op2 = x2 - z2
        Linhas()
        print(f'{x2} - {z2} = {op2}.')
        Linhas()
    elif escolha == 3:
        x3 = float(input('Primeiro número: '))
        z3 = float(input('Segundo número: ')) 
        op3 = x3 * z3
        Linhas()
        print(f'{x3} x {z3} = {op3}.')
        Linhas()
    elif escolha == 4:
        x4 = float(input('Primeiro número: '))
        z4 = float(input('Segundo número: '))
        op4 = x4 / z4
        Linhas()
        print(f'{x4} / {z4} = {op4}.')
        Linhas()
    else:
        print('Escolha uma opção válida.')