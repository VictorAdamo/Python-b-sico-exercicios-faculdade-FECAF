somaNotas = 0
for i in range(4):
    somaNotas += float(input(f'Digite a {i+1}° nota: '))
media = somaNotas/4
print(f'Sua média final é {media}')    