#Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

import math

m2 = float(input('Digite o m² de tinta: '))
l = m2 / 3
latas = math.ceil(l / 18)
print('Precisará de {} latas 18l de tinta e custará {:.2f} R$'.format(latas, latas * 80.0))
