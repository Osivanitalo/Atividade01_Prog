# QUESTAO 3

# Entrada de dados do usuário.
partida_hr    = float (input('Informe o momento inicial da viagem (hora):'))
partida_min   = float (input('Informe o momento inicial da viagem (minuto):'))
partida_seg   = ((partida_hr * 60) * 60) + (partida_min * 60)
chegada_hr    = float (input('Informe o horario da chegada (hora):'))
chegada_min   = float (input('Informe o horario da chegada (minuto):'))
chegada_seg   = ((chegada_hr * 60) * 60) + (chegada_min * 60)
descan_hr     = float (input('Informe o total de tempo de descanso (hora):'))
descan_min    = float (input('Informe o total de tempo de descanso (minuto):'))
descan_seg    = ((descan_hr * 60) * 60) + (descan_min * 60)
dist_perc     = float (input('Informe a distância percorrida em Km: '))
combustivel_l = float (input('Informe o total de litros de combustível gasto na viagem:'))
preco_comb    = float (input('Informe o preço por litro de combustível: R$ '))

# a) o tempo de viagem (em segundos)
if chegada_seg >= partida_seg:
    tempo_viag_seg = chegada_seg - partida_seg
else:
    tempo_viag_seg = (24 * 60 *60) - partida_seg + chegada_seg
    #fiz a multiplicação (24*60*60) para descobrir o total de segundos no dia.

# b) a velocidade média (Km/h) global e a velocidade média em movimento (Km/h)
temp_movim_seg = tempo_viag_seg - descan_seg
temp_movim_hr  = temp_movim_seg / 3600
# aqui eu calculei o tempo em movimento em hr. Dividi o temp em movimt por 3600s
velc_med_global_kmh = dist_perc / (tempo_viag_seg / 3600)
velc_med_movime_kmh = dist_perc / temp_movim_hr

# c) o custo da viagem com combustível (em R$)
cust_viag_reais = preco_comb * combustivel_l

# d) o desempenho do carro (em Km/l, l/h e R$/Km).
desemp_kml = dist_perc / combustivel_l
desemp_litro_hora = combustivel_l / temp_movim_hr
desmp_reais_km = (preco_comb * combustivel_l) / dist_perc

print(f'O tempo total da viagem em segundos foi de: {tempo_viag_seg:.0f}')
print(f'A velocidade média global foi de {velc_med_global_kmh:.2f} km/h, enquanto a velocidade média em movimento foi {velc_med_movime_kmh:.2f} km/h.')
print(f'O custo da viagem com combustível foi de: R$ {cust_viag_reais:.2f}')
print(f'O desempenho do veiculo foi de {desemp_kml:.2f} Km/l, {desemp_litro_hora:.2f} L/hr e {desmp_reais_km:.2f} R$/Km.')
