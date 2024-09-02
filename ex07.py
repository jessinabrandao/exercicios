from datetime import date
anoAtual = date.today().year
while True:
    nascimento = int(input('Ano de Nascimento: '))
    sexo = str(input('SEXO: '))
    idade = anoAtual - nascimento
    print('Quem nasceu em {} tem {} anos de idade'.format(nascimento, idade))

    if idade == 18 and sexo.lower() == 'masculino':
        print('Você deve se alistar')
    elif idade < 18 and sexo.lower() == 'masculino':
        saldo = 18 - idade
        print('Faltam {} para o seu alistamento'.format(saldo))
    elif idade > 18 and sexo.lower() == 'masculino':
        saldo = idade - 18
        print('você deveria ter se alistado há {} atrás'.format(saldo))
    else:
        print('O seu alistamento não é orbrigatório')

    continuar = str(input('Dejesa fazer outra comparação? (s/n)'))
    if continuar.lower() != 's':
        break