
numero = []
for n in range(10):
    numero.append(int(input(f'Digite o {n + 1}° numero: ')))
    for c in numero:
numero.sort(reverse=True)
print(numero)
