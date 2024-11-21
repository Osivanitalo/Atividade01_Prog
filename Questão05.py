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

hr_chegada      = float(input('Informe a hora da chegada: '))
min_chegada     = float(input('Informe os minutos da chegada: '))
tot_min_chegada = (hr_chegada * 60) + min_chegada

hr_saida        = float(input('Informe a hora da saída: '))
min_saida       = float(input('Informe os minutos da saída: '))
tot_min_saida   = (hr_saida * 60) + min_saida

total_permanecia = tot_min_saida - tot_min_chegada
print (f'Você parmaneceu em nosso estacionamento por{total_permanecia:.0f}min')

if total_permanecia <= 60:
    vr_cobrado = 8
elif total_permanecia <= 120:
    vr_cobrado = 8 * 2
elif total_permanecia <= 180:
    vr_cobrado = (8*2) + 5
elif total_permanecia <= 240:
    vr_cobrado = (8*2) + (5*2)
elif total_permanecia <= 720:
    vr_base = (8*2) + (5*2)
    min_extra = total_permanecia - 240 #Aqui eu busquei encontrar os min além dos 240
    hr_extra  = min_extra // 60 #Fiz a divisao inteira, para encontrar a qtd de hr extras
    if min_extra % 60 > 0: #só verificar se tem min restantes (fração de hora)
        # para lembrar, esse % é o resto da divisão inteira
        hr_extra + 1 # add 1h para cada fração, assim consigo somar os $3 por cada hr ou fração
    vr_cobrado = vr_base + hr_extra * 3  
print (f'vr cobrado é de {vr_cobrado} ')


