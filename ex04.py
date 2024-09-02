valor_casa = float(input('Informe o valor da casa R$: '))
salario = float(input('Informe o valor so seu salário R$: '))
tempo = float(input('Em quanto tempo você deseja pagar? '))

prestacao = valor_casa / (tempo * 12)
minimo = salario * 30 / 100
# os 30 se refere aos 30% limite 

if prestacao <= minimo:
    print('Emprestimo concedido')
else:
    print('Emprestimo negado')