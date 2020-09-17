# Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
# Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
# Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.
# 1,5,10,50,100,200

saque = int(input("Digite o Valor que Queres sacar: "))

duzentos = saque // 200
saque = saque % 200
print(saque,duzentos)
cem = saque // 100
saque = saque % 100

cinquenta = saque // 50
saque = saque % 50

dez = saque // 10
saque = saque % 10

cinco = saque // 5
saque = saque % 5


print('{} de 200 R$'.format(duzentos))
print('{} de 100 R$'.format(cem))
print('{} de  50 R$'.format(cinquenta))
print('{} de  10 R$'.format(dez))
print('{} de   5 R$'.format(cinco))
print('{} de   1 R$'.format(saque))