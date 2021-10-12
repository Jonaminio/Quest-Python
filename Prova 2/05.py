def bsort(lista):
    # vai da ultima posição da lista até o indice zero
    for c in range(len(lista), 0, -1):
        # vai da ultima posição da lista até o indice zero
        for atual in range(0, c - 1):
            #faz a troca toda vez q o numero foi maior que p proximo
            #se atual foi maior q o proximo
            if lista[atual] > lista[atual + 1]:
                #faz a troca, o numero atual vai receber o proximo e o proximo recebe o atual
                lista[atual + 1], lista[atual] = lista[atual], lista[atual + 1]

lista1 = [23, 1, 9, 7, 3, 11, 13, 15, 8, 12]
bsort(lista1)
print(lista1)