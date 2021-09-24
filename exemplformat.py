#Faça um programa que peça 2 númueros e some ambos

n1 = float(input('Escreva o primeiro número: '))
n2 = float(input('Escreva o segundo número: '))
soma = n1 + n2

print('A soma dos dois números é %.2f' %soma)
print('A soma de {:.2f} com {:.2f} é igual a {:.2f}' .format(n1,n2, soma))
print(f'A soma de {n1} com {n2} é igual a {soma:.2f}')