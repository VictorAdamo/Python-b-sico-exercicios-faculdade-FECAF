galera = list()
pessoa = dict()
soma = média = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F. ')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:    
        resp = str(input('Quer continuar? [Y/N] ')).upper()[0]
        if resp in 'YN':
            break
        print('ERRO! Digite apenas Y ou N. ')
    if resp == 'N':
        break    
      
média = soma / len(galera)      
print('-=' * 30)
#print(galera)
print(f'A) Número de pessoas cadastras: {len(galera)}')
print(f'B) A média de idade é de {média:5.2f} anos.')
print('C) As mulheres cadastradas foram ', end='')
for i in galera:
    if i['sexo'] == 'F':
        print(f'{i["nome"]} ', end='')    
print()
print(f'D) Lista das pessoas que estão com a idade acima da média: ', end='')
for i in galera:
    if i['idade'] > média:
        print('')
        for k, v in i.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<<ENCEERRADO>>')            
        
