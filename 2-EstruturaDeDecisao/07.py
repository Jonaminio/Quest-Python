#Faça um programa que leia 5 números e informe o maior número.

maior = 0
for c in range(6):
    num = int(input(f'Digite o {c}º numero: '))
    if num > maior:
      maior = num
print(f'O numero Maior é {maior}')
