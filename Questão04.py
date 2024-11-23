# QUESTAO 4

# Entrada de dados do usuário.
dia_inicial = int(input('Informe o dia inicial: '))
mes_inicial = int(input('Informe o mês inicial: '))

dia_final   = int(input('Informe o dia final: '))
mes_final   = int(input('Informe o mês final: '))

if mes_inicial == mes_final:
    diferenca_dias = dia_final - dia_inicial
else:
    diferenca_dias = ((mes_final - mes_inicial) * 30) + (dia_final - dia_inicial)
    #Aqui considerando que todos os meses têm 30 dias.
print (f'Entre as datas informadas passaram-se {diferenca_dias} dia(s).')
