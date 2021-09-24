#Exe01 - Faça um programa que exiba o números de 1 até 10
for i in range(10):
    print(' Número %i' %(i+1))

#Agora 5 vezes indo de 2 em 2, ficando 1,3,5,7 e 9

for i in range(1,10,+2):
    print(' Número %i' %(i))    

#Agora é ao contrário, de 10 até 5, ao invés de +2, usar -1

for j in range(10,4,-1):
    print(' Número %i' %(j)) 

#exemplo de acumulador, note que o print está separado no final, assim a soma aparece apenas no fim do programa
soma=0
for i in range(5):   
    num = int(input('Digite o %i° número: ' %(i+1)))
    soma = soma + num
    print('soma = %i' %(soma))
    

