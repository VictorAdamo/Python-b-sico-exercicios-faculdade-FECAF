#caso for usar um número quebrado use . ao invés de , por exemplo 9.5
nota1 = float(input('Digite a primeira nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
nota3 = float(input('Digite a terceira nota do aluno: '))
media = (nota1 + nota2 + nota3) / 3
if (media <= 4.9) and (media >= 0):
    print('O conceito de média é D ')
elif (media <= 6.9) and (media >= 5):
    print('O conceito de média é C')
elif (media <= 8.9) and (media >= 7):
    print('O conceitp de média é B')
elif (media <= 10) and (media >=9):
    print('O conceito de média é A')    

    

