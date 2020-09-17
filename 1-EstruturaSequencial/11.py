#Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
#o produto do dobro do primeiro com metade do segundo .
#a soma do triplo do primeiro com o terceiro.
#o terceiro elevado ao cubo.

ni1 = int(input("Digite o primeiro numero inteiro: "))
ni2 = int(input('Digite o segundo numero inteiro: '))
n3 = float(input('Digite o numero real: '))
print('A: {} \nB: {}\nC: {}'.format((2 * ni1) * (2 / ni2),3 * ni1 + n3,3 ** n3))