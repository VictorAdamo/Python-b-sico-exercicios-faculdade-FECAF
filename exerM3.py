# usando laço de repetição dentro de outro laço, no exemplo pedindo pra 5 alunos suas notas
aprovados = 0
reprovados = 0
soma = 0
exames = 0
media_da_classe = 0
for i in range(5):

    soma = 0
    nome = input('Digite o nome do %i° aluno: ' %(i+1))
    for j in range(2):
        
        nota = float(input('Digite a %i° nota: ' %(j+1)))
        soma = soma + nota

    media = soma/2
    media_da_classe = media_da_classe + media
    print(' {} Sua media final é %.2f' .format(nome) %(media))
    # ou poderia usar: print(nome 'sua média final é %.2f' %(media))

    if (media >7):
        print('Você foi aprovado com a média %.2f' %(media))
        aprovados = aprovados + 1
    elif (media <=7) and (media >=3):       
        print('Você tera que fazer um exame')
        exames = exames + 1

        exame = float(input('Digite a sua nota de exame: '))
        nova_media = (media+exame)/2
        print('Sua nova média é de %.2f' %(nova_media))

        if (nova_media>7):
            print('Você foi aprovado')
            aprovados = aprovados + 1
        else:
            print('Você foi reprovado')
            reprovados = reprovados + 1 
    else:
        print('Você foi reprovado com a média %.2f' %(media))
        reprovados = reprovados + 1         

media_da_classe = media_da_classe/5
print('-=' * 30)
print('Número de aprovados é %i' %(aprovados))
print('Número de reprovados é %i' %(reprovados))
print('Número de exames é %i' %(exames))
print('Média da classe é %.2f' %(media_da_classe))  

