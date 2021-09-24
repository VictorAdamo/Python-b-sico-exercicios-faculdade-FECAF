salario = float(input('Digite seu salário: '))
temposerv = int(input('Digite quantos anos de serviço você tem: '))
if temposerv > 5:
    aum = salario * 15/100
    print('Seu aumento de salário é de 15%')
    print('Seu novo salário é de %.2f' %(salario+aum))
else:
    aum = salario * 10/100
    print('Seu aumento de salário é de %.2f' %aum )
    print('Seu novo salário é de %.2f' %(salario+aum)) 
