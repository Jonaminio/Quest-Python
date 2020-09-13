#Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
#C = 5 * ((F-32) / 9).

f = float (input('Digite a temperatura em Fº: '))
print('A temperatura {}Fº é ===> {}Cº <==='.format(f,(5*(f-32)/9)))