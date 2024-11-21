#QUESTAO 05


hr_chegada      = float(input('Informe a hora da chegada: '))
min_chegada     = float(input('Informe os minutos da chegada: '))
tot_min_chegada = (hr_chegada * 60) + min_chegada

hr_saida        = float(input('Informe a hora da saída: '))
min_saida       = float(input('Informe os minutos da saída: '))
tot_min_saida   = (hr_saida * 60) + min_saida

if tot_min_saida < tot_min_chegada:
    tot_min_saida += 24 * 60 #Aqui somente nos casos da saida no dia seguinte. Add + 24h
    #Usei a mesma lógica da questão 3. Chegada > saida, add 24h.

total_permanecia = tot_min_saida - tot_min_chegada

print (f'Você parmaneceu em nosso estacionamento por {total_permanecia:.0f}min')

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
        hr_extra += 1 # add 1h para cada fração, assim consigo somar os $3 por cada hr ou fração
        #consegui consertar adicionando o =, pois a cada hr ou fração tem que somar +3.
    vr_cobrado = vr_base + hr_extra * 3
else:
    vr_cobrado = 30
    print (f'Você permaneceu em nosso estacionamento por um periodo igual ou superior a 12h.')

print (f'Valor a ser pago é de R$ {vr_cobrado:.0f} ')