idade = int(input('Informe a sua idade: '))

def verificar(idade):
    if (idade >= 18):
        print('Você pode tirar a habilitação.')
    else: 
        print('Você não pode tirar a habilitação.')

#status = "sucesso" if saldo <= saque else "falha"
#print(f"{status} ao realizar o saque!")
        

verificar(idade)