#Faça um Programa que leia três números e mostre-os em ordem decrescente.

num1 = int(input('Digite o Primeiro numero: '))
num2 = int(input('Digite o Primeiro numero: '))
num3 = int(input('Digite o Primeiro numero: '))

if num1 > num2 and num1 > num3:
    maior = num1
    if num2 > num3:
        meio = num2
        menor = num3
    else:
        meio = num3
        menor = num2
if num2 > num1 and num2 > num3:
    maior = num2
    if num1 > num3:
        meio = num1
        menor = num3
    else:
        meio = num3
        menor = num1
if num3 > num2 and num3 > num1:
    maior = num3
    if num2 > num1:
        meio = num2
        menor = num1
    else:
        meio = num1
        menor = num2

print('{},{},{}'.format(maior, meio, menor))
