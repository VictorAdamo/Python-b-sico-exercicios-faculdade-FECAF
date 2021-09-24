import os
from time import sleep
couves=0
roela=0
nocao=0
branco=0
nulo=0
galera = list()
pessoa = dict()
soma = 0
média = 0
while True:
    print('===== ELEIÇÃO 2021 =====')
    print('Escolha seu candidato: 1-Zé das Couves, 2-Zé Roela, 3-Sem noção, ')
    print('4-Em branco, 5-Nulo')
    pessoa.clear()
    pessoa['nome'] = str(input('Digite seu nome: '))
    while True:
        pessoa['sexo'] = str(input('Digite seu sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('Erro, digite apenas M ou F. ')
    pessoa['idade'] = int(input('Digite sua idade: '))
    soma += pessoa['idade']
    while True:
        pessoa['opcao'] = input('Digite seu voto: ')
        if(pessoa['opcao'] == '1'):
            couves+= 1
            break    
        elif(pessoa['opcao'] == '2'):
            roela+=1
            break    
        elif(pessoa['opcao'] == '3'):
            nocao+=1
            break    
        elif(pessoa['opcao'] == '4'):
            branco+=1
            break    
        elif(pessoa['opcao'] == '5' ):
            nulo+=1
            break
        else:
            print('ERRO, digite apenas números válidos. ') 
    galera.append(pessoa.copy())
    while True:    
        resp = str(input('Quer continuar? [Y/N] ')).upper()[0]
        if resp in 'YN':
            break
        print('ERRO! Digite apenas Y ou N. ')
    if resp == 'N':
        break
    os.system('cls')
média = soma / len(galera)     
os.system('cls')    
print("===== RESULTADO DAS ELEIÇÕES =====")
print(f'Número de pessoas que votaram: {len(galera)}')
print(f'O número de votos para o Zé das Couves foram {couves} ')
print(f'O número de votos para o Zé Roela foram {roela} ')
print(f'O número de votos para o Sem Noção foram {nocao} ')
print(f'O número de votos para em branco foram {branco} ')
print(f'O número de votos nulos foram {nulo} ')
print('=' * 30)
print('As mulheres que votaram foram: ')
for i in galera:
    if i['sexo'] == 'F':        
        print(f'{i["nome"]} ')        
print('Os homens que votaram foram: ')
for i in galera:
    if i['sexo'] == 'M':
        print(f'{i["nome"]} ')  
if (len(galera)) > 1:    
    print(f'A média de idade das pessoas cadastradas é de {média:5.2f} anos.')             
print('<<FIM DO PROGRAMA>>')                            
sleep(15)

