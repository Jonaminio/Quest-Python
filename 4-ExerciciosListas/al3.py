numeros = []

while True:
    numeros.append(int(input('Digite o numero a ser add: ')))
    sair = int(input('Deseja adicionar mais? 1 - Sim, 0 = Sair: '))
    if sair == 0:
        break

print(numeros)
