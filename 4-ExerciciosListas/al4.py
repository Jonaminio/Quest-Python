lista = []
pares = []
impar = []
while True:
    lista.append(int(input("Digite um numero a ser adicionado: ")))
    resp = str(input("Queres continuar? [S] = para sim e [N] para não: "))
    if resp == 'N' or resp == 'n':
        break
print(lista)
#para o indice no valor em lista enumerada faça
for indice,valor in enumerate(lista):
    print(f"valor de Indice: {indice}")
    print(f"Valor de valor de lista? : {valor}")
    if valor % 2 == 0:
            pares.append(valor)
    else:
            impar.append(valor)
print(pares)
print(impar)
