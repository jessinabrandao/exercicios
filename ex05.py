while True:
    inteiro = int(input('Digite um número inteiro: '))
    print('''Selecione uma opção: 
        [1] BINÁRIO
        [2] OCTAL
        [3] HEXADECIMAL''')

    opcao = int(input('SUA OPÇÃO: '))

    if opcao == 1:
        print('{} convertido para BINÁRIO é igual a {}'.format(inteiro, bin(inteiro)))
    elif opcao == 2:
        print('{} convertido para OCTAL é igual a {}'.format(inteiro, oct(inteiro)))
    elif opcao == 3:
        print('{} convertido para HEXADECIMAL é igual a {}'.format(inteiro, hex(inteiro)))
    else:
        print('OPÇÃO INVÁLIDA')
    
    continuar = input("Deseja realizar outra conversão? (s/n): ")
    if continuar.lower() != 's':
        break