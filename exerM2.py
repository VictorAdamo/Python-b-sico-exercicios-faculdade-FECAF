# usando laço de repetição dentro de outro laço, no exemplo pedindo pra 5 alunos suas notas
soma = 0
for i in range(5):

    soma = 0
    nome = input('Digite o nome do %i° aluno: ' %(i+1))
    for j in range(3):
        
        nota = float(input('Digite a %i° nota: ' %(j+1)))
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
            