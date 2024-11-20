#QUESTAO 05

'''
Em um estacionamento, as tarifas são as seguintes (cumulativas):
• Até duas horas: R$ 8,00/hora ou fração;
• Entre três e quatro horas: R$ 5,00/hora ou fração;
• Horas seguintes: R$ 3,00/hora ou fração.
• Depois de 12h, o custo passa a ser fixo: R$ 30,00

Faça um programa que leia o número de minutos que um veículo permaneceu no estacionamento e exiba
o valor a ser pago pelo responsável.

Como exemplo, considere que o carro ficou 310 minutos no estacionamento; deve pagar: R$ 16,00
(pelas duas primeiras horas) + R$ 10,00 (pela terceira e quarta horas) + R$ 6,00 
(pela quinta hora e fração da sexta hora): total de R$ 32,00
'''

hr_chegada      = float ((input 'Informe a hora da chegada: '))
min_chegada     = float ((input 'Informe os minutos da chegada: '))
tot_min_chegada = (hr_chegada * 60) + min_chegada

hr_saida        = float ((input 'Informe a hora da saída: '))
min_saida       = float ((input 'Informe os minutos da saída: '))
tot_min_saida   = (hr_saida * 60) + min_saida

total_permanecia = tot_min_chegada + tot_min_saida