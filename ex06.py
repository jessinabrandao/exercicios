while True:
    num1 = int(input('Informe um valor inteiro: '))
    num2 = int(input('Informe outro valor inteiro: '))

    if num1 > num2:
        print('{} é MAIOR que {}'.format(num1, num2))
    elif num1 < num2:
        print('{} é MENOR que {}'.format(num1, num2))
    else:
        print('{} é IGUAL a {}'.format(num1, num2))
    
    continuar = str(input('Dejesa fazer outra comparação? (s/n)'))
    if continuar.lower() != 's':
        break
print('Tenha um bom dia!')