#Faça um programa que leia 5 números e informe a soma e a média dos números.

soma = 0
for c in range(1,6):
    numero = int(input(f'Digite o {c}º Numero: '))
    soma = soma + numero
print(f'A Soma dos numeros são: {soma}')
print(f'A média dos numeros são: {soma/5}')