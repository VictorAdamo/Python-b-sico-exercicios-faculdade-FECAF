sal1 = float(input('Digite seu salário: '))
#newsal = sal1 + sal1 * 5/100
aum = sal1 * 5/100
if sal1 > 5000:
    print('Você tem o direito de aumento de 5% ')
    print('Seu aumento é de %.2f ' %aum)
    print('Seu novo salário é de %.2f ' %(sal1+aum))    
else:
    print('Você não tem o direito de um aumento ')    
