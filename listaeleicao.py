import os
couves=0
roela=0
nocao=0
branco=0
nulo=0
el =0
while True:
    print('===== ELEIÇÃO 2021 =====')
    print('Escolha seu candidato: 1-Zé das Couves, 2-Zé Roela, 3-Sem noção, ')
    print('4-Em branco, 5-Nulo')    
    while True:
        opcao = int(input('Digite sua opção: '))    
        if(opcao == 1):
            couves+= 1
            break    
        elif(opcao ==2):
            roela+=1
            break    
        elif(opcao==3):
            nocao+=1
            break    
        elif(opcao==4):
            branco+=1
            break    
        elif(opcao==5):
            nulo+=1
            break
        else:
            print('ERRO, digite apenas números válidos. ')                           
    while True:
        el += 1    
        resp = str(input('Quer continuar? [Y/N] ')).upper()[0]
        if resp in 'YN':
            break
        print('ERRO! Digite apenas Y ou N. ')
    if resp == 'N':
        break
    os.system('cls')
os.system('cls')                       
print("===== RESULTADO DAS ELEIÇÕES =====")
print("Total de votos para o Zé das Couves %i " %(couves))
print("Total de votos para o Zé Roela %i " %(roela))
print("Total de votos para o Sem Noção %i " %(nocao))
print("Total de votos em branco %i " %(branco))
print("Total de votos nulos %i " %(nulo))
print('O número de eleitores é {}' .format(el))
print('Porcentagem de votos para o Zé das Couves é de {:.2f}%'.format(couves*100/el))
print('Porcentagem de votos para o Zé Roela é de {:.2f}%'.format(roela*100/el))
print('Porcentagem de votos para o Sem Noção é de {:.2f}%'.format(nocao*100/el))
print('Porcentagem de votos para em branco é de {:.2f}%'.format(branco*100/el))
print('Porcentagem de votos para nulo é de {:.2f}%'.format(nulo*100/el))
