fi = 0
somafi = 0
somasal = 0
contmenos100 = 0
contpo = 0
sal = 0
while sal >= 0:
    sal = float(input('Digite o valor do seu sálario: '))
    contpo += 1
    somasal += sal
    if (sal <= 100) and (sal >= 0):
        contmenos100 += 1
    fi = int(input('Digite o número de quantos filhos vc tem: '))
    somafi += fi
mediasal = somasal/contpo
mediafi = somafi/contpo
percentual100 = (contmenos100/contpo) * 100
print('=' * 30)
print(f'A média do salário da população é de R${mediasal:5.2f}')
print(f'A média do número de filhos é de {mediafi:.2f}%')
print(f'O percentual de pessoas com salário até R$100,00 é de {percentual100:.2f}%')
    