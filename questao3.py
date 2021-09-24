num = 1000
contresto5 = 0

while num <= 1999:
    if num % 11 == 5:
        contresto5 += 1
    print(num)
    num += 1
print(f'O número de números que divididos por 11 da resto igual a 5 é: {contresto5} ')    