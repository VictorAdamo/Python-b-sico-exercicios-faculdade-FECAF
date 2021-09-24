#contador de pares 100 a 200
num = 100
cont_pares = 0

while num <=200:
    if num % 2 == 0:
        cont_pares += 1
    num += 1   
print(f'Quantidade de pares é: {cont_pares}')          