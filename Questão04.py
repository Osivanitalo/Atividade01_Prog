# QUESTAO 4

'''
 O número de dias decorridos entre duas datas é importante em uma infinidade de
situações da vida cotidiana. Faça um programa que recebe inicialmente dois valores (dia inicial 
e mês inicial), depois mais dois valores (dia final, mês final), ao final deve indicar quantos 
dias se passaram entre as datas (considere que o ano não é bissexto).

Exemplos:
o 02 de 05 até 03 de 05 - 1 dia
o 27 de 04 até 03 de 05 - 6 dias
o 03 de 02 até 03 de 05 - 90 dias
Não esqueça de verificar se a data inicial é menor ou igual à data final.

Dica: conte o número de dias até cada uma das datas e subtraia esses números.
'''

dia_inicial = int(input('Informe o dia inicial (com dois dígitos): '))
mes_inicial = int(input('Informe o mês inicial (com dois dígitos): '))

dia_final   = int(input('Informe o dia final (com dois dígitos): '))
mes_final   = int(input('Informe o mês final (com dois dígitos): '))

if mes_final == mes_final:
    diferenca_dias = dia_final - dia_inicial
else:
    diferenca_dias = ((mes_final - mes_inicial) * 30) - (dia_final - dia_inicial)
    #Aqui considerando que todos os meses têm 30 dias.
print (f'Entre as datas {dia_inicial'/'mes_inicial} e {dia_final'/'mes_final} passaram-se {diferenca_dias}.')