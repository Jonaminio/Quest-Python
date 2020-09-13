#Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#Para homens: (72.7*h) - 58
#Para mulheres: (62.1*h) - 44.7

altura = float (input('Digite sua Altura: '))
s = int (input('Digite 1 para Homem e 2 para Mulher: '))
if s == 1:
    print('Seu peso ideal é: {:.2f}'.format(72.7 * altura - 52))
else:
    print('Seu peso ideal é: {:.2f}'.format(62.1 * altura - 44.7))