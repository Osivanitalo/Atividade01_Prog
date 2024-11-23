# QUESTAO 06

from datetime import datetime
import sys

# Entrada de dados do usúario.
genero        = str(input('Informe o genero do(a) contribuinte (Masculino/Feminino):'))
nascimento    = str(input('Informe a data de nascimento no formato (DD/MM/AAAA):'))
data_ini_cont = str(input('Informe a data do inicio da sua contribuição (DD/MM/AAAA):'))
#Quando rodei o cod para teste, informou que era um str e não float.

nascimento    = datetime.strptime(nascimento, '%d/%m/%Y')
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

#calcular a aposentadoria por idade e por tempo contribuição
data_apost_por_idade = datetime (nascimento.year + idade_minima, nascimento.month, nascimento.day)
data_apost_por_tempo = datetime (data_ini_cont.year + tempo_cont, data_ini_cont.month, data_ini_cont.day)
#saber a data exata que vai atingir a idade minima da aposent. O .year é calcular o ano

#Segunda condição é saber se tem pelo menos 15 anos de contribuição, independente do sexo.
data_min_contrib = datetime (data_ini_cont.year + 15, data_ini_cont.month, data_ini_cont.day)

'''
Verificar se a o contrinuinte atingiu a idade minima com a condição de no mínimo 
15 anos de contribuição.
'''
if data_apost_por_idade < data_apost_por_tempo:
    data_apost_por_idade = data_min_contrib

#Atribuir qual a data mais longe (idade ou contribuição) para ser informada.
if data_apost_por_idade > data_apost_por_tempo:
    data_aposentadoria = data_apost_por_idade
else:  
    data_aposentadoria = data_apost_por_tempo

print(f'O(A) contribuinte poderá se aposentar em {data_aposentadoria.strftime('%d/%m/%Y')}')
'''
Aqui foi usado o strftime('%d/%m/%Y'), pois eu quero que a data seja apresentada no formato
brasileiro (DD/MM/AAAA).
'''