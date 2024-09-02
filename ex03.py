opção = -1

while opção != 0:
    numero = int(input('informe um número: '))

    if numero % 2 == 0:
        print('fazer algo')
        if numero == 10: 
            break
    
    elif numero % 2 != 0:
        print('ola')
    