import random
bitela = ['TCHOLA', 'VIK', 'KAILIN', 'CHAPOCA', 'GAGA']
escolhido = random.choice(bitela)
palpite = str(0)
t = 0

print('Chute o bitelinha')
print('Chute entre: Tchola, Vik, Kailin, Chapoca ou Gaga')
while palpite != escolhido:
    palpite = input('Digite o nome do bitela: ').strip().upper()
    t +=1
    if palpite == escolhido:
        print('-=' * 30)
        print('Parabens!!! Você acertou o bitela é o {}!' .format(escolhido))
        print(f'Acertou! Placar de {t}')
    else:
        print('Errou tente novamente')
        print(' O bitela não é o {}' .format(palpite))        