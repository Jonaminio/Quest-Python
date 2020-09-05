base = int(input('Digite a Base que deseja calcular:'))
expo = int(input('Digite o expoente que deseja calcular: '))
valor: int = 0
for c in range(expo):
    valor = valor + (base * expo)

print(f'O numero é: {valor}')
