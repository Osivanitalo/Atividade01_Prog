# Questão_02

valor_saque = float(input('Informe o valor do saque R$:'))
if valor_saque <= 0:
    print ('O valor do saque deve ser igual ou superior a R$ 0,01!')
elif valor_saque > 5000:
    print ('O valor máximo por saque é de até R$5.000,00.')
   
else:
    cedula_100  = valor_saque // 100
    valor_saque = valor_saque % 100

    cedula_50   = valor_saque // 50
    valor_saque = valor_saque % 50

    cedula_20   = valor_saque // 20
    valor_saque = valor_saque % 20

    cedula_10   = valor_saque // 10
    valor_saque = valor_saque % 10

    cedula_5    = valor_saque // 5
    valor_saque = valor_saque % 5

    cedula_2    = valor_saque // 2
    valor_saque = valor_saque % 2

    moeda_1     = valor_saque // 1
    valor_saque = valor_saque % 1

    moeda_050   = valor_saque // 0.50
    valor_saque = valor_saque % 0.50

    moeda_025   = valor_saque // 0.25
    valor_saque = valor_saque % 0.25

    moeda_010   = valor_saque // 0.10
    valor_saque = valor_saque % 0.10

    moeda_005   = valor_saque // 0.05
    valor_saque = valor_saque % 0.05

    moeda_001   = valor_saque / 0.01
    valor_saque = valor_saque % 0.01

    print (f'Quantidade de notas de R$ 100: {cedula_100:.0f}')
    print (f'Quantidade de notas de R$ 50: {cedula_50:.0f}')
    print (f'Quantidade de notas de R$ 20: {cedula_20:.0f}')
    print (f'Quantidade de notas de R$ 10: {cedula_10:.0f}')
    print (f'Quantidade de notas de R$ 5: {cedula_5:.0f}')
    print (f'Quantidade de notas de R$ 2: {cedula_2:.0f}')
    print (f'Quantidade de moeda de R$ 1: {moeda_1:.0f}')
    print (f'Quantidade de moeda de R$ 0.50: {moeda_050:.0f}')
    print (f'Quantidade de moeda de R$ 0.25: {moeda_025:.0f}')
    print (f'Quantidade de moeda de R$ 0.10: {moeda_010:.0f}')
    print (f'Quantidade de moeda de R$ 0.05: {moeda_005:.0f}')
    print (f'Quantidade de moeda de R$ 0.01: {moeda_001:.0f}')