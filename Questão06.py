# QUESTAO 06

'''
Com base na nova legislação da Previdência Brasileira, regulamentada pela Lei
Complementar nº 1354/2020 e pela Emenda à Constituição nº 49/2020, desenvolva um programa em
Python que solicite as seguintes informações de uma pessoa:
• Sexo da pessoa (masculino/feminino).
• Data de nascimento da pessoa (no formato DD/MM/AAAA).
• Data de início da contribuição previdenciária da pessoa (no formato DD/MM/AAAA).

O programa deve então calcular e exibir a data em que a pessoa poderá se aposentar, considerando as
seguintes regras:
• Aposentadoria por Idade:
o Homens podem se aposentar aos 65 anos de idade.
o Mulheres podem se aposentar aos 62 anos de idade.
o É necessário ter pelo menos 15 anos de contribuição.
• Aposentadoria por Tempo de Contribuição:
o Homens podem se aposentar após 35 anos de contribuição.
o Mulheres podem se aposentar após 30 anos de contribuição.

Implemente o programa em Python para calcular a data de aposentadoria e exibi-la como resultado.

Dica: Utilize as bibliotecas datetime e dateutil.
'''
from datetime import datetime
from dateutil import dateutil
import sys


genero = str(input('Informe o genero do contribuinte (Masculino/Feminino):'))
nascimento = float(input('Informe a data de nascimento no formato (DD/MM/AAAA):'))
data_ini_cont = float(input('Informe a data do inicio da sua contribuição (DD/MM/AAAA):'))

nascimento = datetime.strptime(nascimento, '%d/%m/%Y')
data_ini_cont = datetime.strptime(data_ini_cont, '%d/%m/%Y')

if genero == 'Masculino':
    idade_minima = 65
    tempo_cont = 35
elif genero == 'Feminino':
    idade_minima = 62
    tempo_cont = 30
else:
    print('Genero inválido. Informe "Masculino" ou "Feminino"!')
    sys.exit