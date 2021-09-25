def pedirDatas(dicionario):
    print('Preenchendo...')
    dicionario['SEGUNDA'] = int(input('Digite a data de segunda-feira: '))
    dicionario['TERÇA'] = int(input('Digite a data de terça-feira: '))
    dicionario['QUARTA'] = int(input('Digite a data de quarta-feira: '))
    dicionario['QUINTA'] = int(input('Digite a data de quinta-feira: '))
    dicionario['SEXTA'] = int(input('Digite a data de sexta-feira: '))
    dicionario['SÁBADO'] = int(input('Digite a data de sábado: '))
    dicionario['DOMINGO'] = int(input('Digite a data de domingo: '))
    print('-' * 10)

def mostrarDatas(dicionario):
    print(dicionario)
    print('-' * 10)
    for k, v in dicionario.items():
        print(f'{k} é dia {v}')
    print('-' * 10)

def buscarData(dicionario):
    for elemento in dicionario:
        busca = input('Digite o dia da semana que deseja saber a data: ').upper()
        print(f'{busca} é dia: {dicionario.get(busca)}')
        break




