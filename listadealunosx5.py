Turma = list()
alunos = dict()
for i in range(5):
    alunos.clear()
    alunos['nome'] = str(input('Digite o nome do %i° aluno: ' %(i+1)))
    while True:
        alunos['sexo'] = str(input('Digite o sexo do %i° aluno, [M/F]: ' %(i+1))).upper()[0]
        if alunos['sexo'] in 'MF':
            break
        print('Erro! Por favor digite apenas M ou F')  
    alunos['idade'] = int(input('Digite a idade do {}° aluno: ' .format(i+1)))
    Turma.append(alunos.copy())
    
    # ou poderia ser:
    # aluno = str(input('Digite o nome do {}° aluno: ' .format(i+1)))
print('-=' * 30)    
print(f'Lista de alunos: {Turma}') 