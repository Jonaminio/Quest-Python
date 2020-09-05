import math

m2 = float(input('Digite o m² de tinta: '))
l = m2 / 3
latas = math.ceil(l / 18)
print('Precisará de {} latas 18l de tinta e custará {:.2f} R$'.format(latas, latas * 80.0))
