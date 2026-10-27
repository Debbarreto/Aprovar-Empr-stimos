#Aprovar Empréstimos
print('Bem vindo ao CREDPAY! Seu lugar de Empréstimos Seguros!')
nome=input('Para iniciarmos o atendimento: Qual o seu nome?')
print(nome,', que bom ter você com a CREDPAY!')
casa = float(input('Qual o valor da casa desejada? R$'))
salario = float(input('Qual o seu salário? R$'))
anos = int(input('Quantos anos de financiamento?'))
prestacao = casa / (anos * 12)
limite = salario * 30/100
if prestacao <= limite:
    print("\nEmpréstimo APROVADO!")
    print(f"Prestação mensal: R$ {prestacao:.2f}")
else:
    print("\nEmpréstimo NEGADO!")
    print(f"Prestação mensal: R$ {prestacao:.2f}")
    print(f"O limite permitido é R$ {limite:.2f}")
