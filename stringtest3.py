def Linhas():
    print('-=' * 15)

bitela = 'PITOLA'
Acertou = False
Palpites = 0
Linhas()
print('O Bitela é o Pitola ou o Nina?')
Linhas()
while not Acertou:
    jogador = str(input('Digite quem é o bitela: ')).strip().upper()
    Palpites += 1    
    if jogador == bitela:
        Acertou = True
    else:
        print(f'Tente novamente, o bitela não é o {jogador}')    
Linhas()
print(f'Parabéns vc acertou o bitela é o {bitela}!')
print(f'Vc acertou com o número de {Palpites} Palpites')
Linhas()