maior = 0
for c in range(6):
    num = int(input(f'Digite o {c}º numero: '))
    if num > maior:
      maior = num
print(f'O numero Maior é {maior}')
