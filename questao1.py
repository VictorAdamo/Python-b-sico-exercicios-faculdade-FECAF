
sltnps = 0
smaltm = 0
nm = 0
nh= 0
shalt = 0
for i in range(50):
    pessoa = str(input('Digite seu nome: '))
    #altura coloque um ., como 1.81
    altura = float(input('Digite sua altura: '))
    sexo = str(input('Digite seu sexo M/F: ')).upper()[0]
    sltnps += altura
    if sexo == 'F':
        nm += 1
        smaltm += altura
    elif sexo == 'M':
        nh += 1
        shalt += altura
mediah = shalt/nh
mediam = smaltm/nm
mediasala = sltnps/50
print('A média da altura das mulheras da sala é de {:.2f} altura' .format(mediam))
print('A média da altura dos homens da sala é de {:.2f} altura'.format(mediah))
print('A média de altura da turma é de {:.2f} altura'.format(mediasala))