def numerosd(numeros):
    impar = []
    pares = []
    for indice, valor in enumerate(numeros):
        if valor % 2 == 0:
            pares.append(valor)
        else:
            impar.append(valor)
    print(impar)


numeros = []

while True:
    numeros.append(int(input('Digite o numero a ser add: ')))
    sair = int(input('Deseja adicionar mais? 1 - Sim, 0 = Sair: '))
    if sair == 0:
        break

numerosd(numeros)
