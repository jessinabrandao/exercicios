num_provas = int(input('Digite o númmero de provas: '))
soma = 0

for i in range(num_provas):
    nota = float(input('Digite a nota da prova: '))
    soma +=  nota

media = soma / num_provas

print('Sua média é: {}'.format(media))