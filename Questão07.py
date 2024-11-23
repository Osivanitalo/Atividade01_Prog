# QUESTAO 07

import math

#Identificação dos lados:
lado_a = float(input('Informe o cumprimento do lado A:'))
lado_b = float(input('Informe o cumprimento do lado B:'))
lado_c = float(input('Informe o cumprimento do lado C:'))

if lado_a + lado_b <= lado_c:
    print('Os lados informados não podem formar um triângulo!')
elif lado_a + lado_c <= lado_b:
    print('Os lados informados não podem formar um triângulo!')
elif lado_b + lado_c <= lado_a:
    print('Os lados informados não podem formar um triângulo!')
else:
    print('Os lados informados podem formar um triângulo!')
# A soma de dois lados precisam ser maior que o terceiro lado.

'''
calcular conforme a lei dos cossenos:
Ângulo a = ((b² + c² - a²) / (2 * b * c))
Ângulo b = ((a² + c² - b²) / (2 * a * c))
Ângulo c = ((a² + b² - c²) / (2 * a * b))
'''

angulo_a = math.degrees(math.acos((lado_b**2 + lado_c**2 - lado_a**2) / (2*lado_b*lado_c)))
angulo_b = math.degrees(math.acos((lado_a**2 + lado_c**2 - lado_b**2) / (2*lado_a*lado_c)))
angulo_c = math.degrees(math.acos((lado_a**2 + lado_b**2 - lado_c**2) / (2*lado_a*lado_b)))
# O math.degrees é para informar que quero o calculo em Graus.
# O math.acos é para informar que quero o calculo do arco do cosseno.

print(f'Os ângulos do triângulo são: A {angulo_a:.2f}°, B {angulo_b:.2f}° e C {angulo_c:.2f}°.')

'''
Classificação dos triângulos:
três lados são iguais (equilátero);
se dois lados são iguais (isósceles);
se todos os lados são diferentes (escaleno).
'''
if lado_a == lado_b:
    if lado_b == lado_c:
        classificacao = 'Equilátero.'
    elif lado_a == lado_b:
        classificacao = 'Isósceles.'
    elif lado_b == lado_c:
        classificacao = 'Isósceles.'
    elif lado_a == lado_c:
        classificacao = 'Isósceles.'
else:
    classificacao = 'Escaleno.'
print(f'O triângulo é classificado como {classificacao}.')
