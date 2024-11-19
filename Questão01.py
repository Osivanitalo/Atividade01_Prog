# Questão_01

numero = int(input('Informe um valor de até 4 algarismos:'))
if numero <= 0:
    print('Digite um número maior que 0!')
elif numero > 9999:
    print('Digite um númeto com no máximo 4 dígitos!')
else:
    m      = numero // 1000
    numero = numero % 1000

    c      = numero // 100
    numero = numero % 100

    d      = numero // 10
    numero = numero % 10

    u      = numero // 1
    numero = numero % 1  
    
    soma   = m + c + d + u
    print (f'A soma dos algarismos é: {soma}')
