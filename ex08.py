while True:
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2

    if media >= 7:
        print('sua média é {} você foi aprovado'.format(media))
    elif media >=4 and media <=6:
        print('Sua média é {} você está na final'.format(media))
    else:
        print('Você foi reprovado')
    
    continuar = str(input('Deseja realizar outra operação? (s/n)'))
    if continuar.lower() != 's':
        break
    