# QUESTAO 07

# Achar a regra que diz se os lados podem formar um triangulo

'''
O input é La / Lb / Lc
La = int (input('informe La'))
La <0
Lb <0
Lc <0
se passou por isso, é que vou saber se forma um triangulo. 


Após indentificar que é um triangulo, será possivel identificar os três angulos.
É para calcular os três.

Classificar o triangulo, quanto aos lados: Equilátero (3 lados igual), 
isósceles (2 lados iguais), escaleno (nenhum lado igual)

Classificar o triangulo, quanto aos ângulo: (agudo, obtuso ou retângulo)
'''

'''
Desenvolva um código em Python que solicite ao usuário que informe os
comprimentos dos três lados de um triângulo. Em seguida, verifique se esses comprimentos podem
formar um triângulo. Caso afirmativo, calcule e informe os valores dos ângulos do triângulo 
e classifiqueo quanto aos lados e aos ângulos.

• Instruções:
a) Peça ao usuário para inserir os comprimentos dos três lados do triângulo.
b) Verifique se os comprimentos fornecidos podem formar um triângulo. Caso contrário, informe
que não é possível formar um triângulo com esses lados.
c) Se for possível formar um triângulo, calcule os três ângulos do triângulo.
d) Classifique o triângulo quanto aos lados (equilátero, isósceles ou escaleno) e aos ângulos
(agudo, obtuso ou retângulo).
e) Exiba a classificação do triângulo quanto aos lados e aos ângulos.

• Observações:
o Para determinar se os lados fornecidos pelo usuário podem formar um triângulo, é necessário
verificar a seguinte condição: A soma de quaisquer dois lados de um triângulo deve ser
sempre maior que o terceiro lado.
o Você pode usar a Lei dos cossenos para calcular os ângulos de um triângulo.
o Para classificar quanto aos lados, verifique se os três lados são iguais (equilátero), se dois
lados são iguais (isósceles) ou se todos os lados são diferentes (escaleno).
o Para classificar quanto aos ângulos, verifique se um dos ângulos é maior que 90 graus
(obtuso), se um dos ângulos é igual a 90 graus (retângulo) ou se todos os ângulos são
menores que 90 graus (agudo).
o Considere que os ângulos são expressos em graus.
Desenvolva o código em Python para atender às especificações acima.

Dica: Utilize a biblioteca math.
'''

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