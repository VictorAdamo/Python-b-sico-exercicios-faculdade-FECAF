#faça um programa que peça 5 números e conte quantos números são pares
cont = 0
contim = 0
somapares = 0
somaim = 0
for i in range(5):
    num = int(input('Digite o {}° número: '.format(i+1)))
    # ou utilizar:
    #num = int(input('Digite o %i° número: ' %(i+1)))    
    if(num % 2 == 0):
        somapares += num
        cont= cont+1
    else:
        somaim += num
        contim= contim+1   
    
print('número de números pares é %i' %(cont))
print('A soma dos números pares é {} ' .format(somapares))   
print('número de números impars é %i' %(contim))
print('A soma dos números impars é {} ' .format(somaim)) 
         