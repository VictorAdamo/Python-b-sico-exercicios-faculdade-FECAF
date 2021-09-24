import random
bitela = ['TCHOLA', 'TARKUS', 'CHAPOCA', 'VIK', 'KAILIN', 'GAGA']
escolhido = random.choice(bitela)
print('Chute o bitela')
print('Chute entre Tchola, Tarkus, Chapoca, Vik, Kailin ou Gaga')
acertou = False
palpites = 0
while not acertou:
    jogador = str(input('Digite o nome do bitela: ')).strip().upper()
    palpites +=1
    if jogador == escolhido:
        acertou = True
    else:
        print('Chute novamente, o bitela não é o {}' .format(jogador))
print('-=' * 15)
print(f'Parabéns você acertou, o bitela é o {escolhido} ')
print(f'Acertou com o placar de {palpites}')            