#Exercicio media aritmetica com laço de repetição
# usando laço de repetição
nome = input('Digite seu nome: ')
soma = 0
for i in range(3):
    nota = float(input('Digite a %i° nota: ' %(i+1)))
    soma = soma + nota

media = soma/3
print(' {} Sua media final é %.2f' .format(nome) %(media))
# ou poderia usar: print(nome 'sua média final é %.2f' %(media))

if (media >=6):
    print('Você foi aprovado com a média %.2f' %(media))
else:
    print('Você foi reprovado com a média %.2f' %(media))
    print('Você tera que fazer um exame')

    exame = float(input('Digite a sua nota de exame: '))
    nova_media = (media+exame)/2
    print('Sua nova média é de %.2f' %(nova_media))

    if (nova_media>=6):
        print('Você foi aprovado')
    else:
        print('Reprovado')    


# sem usar laço de repetição: 

#faça um programa que peça duas notas do aluno.
#calcule a média aritmética
#mostre se ele está aprovado ou não. A média da aprovação
#tem que ser maior ou igual a 6

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) /2

if (media >=6):
    print('Você foi aprovado com média %.1f' %(media))
else:
    print('Você foi reprovado com média %.1f' %(media))