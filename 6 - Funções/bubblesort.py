def bsort(lista):

    for final in range(len(lista), 0, -1):
        exchanging = False

        for current in range(0, final - 1):
            if lista[current] > lista[current + 1]:
                lista[current + 1], lista[current] = lista[current], lista[current + 1]
                exchanging = True

        if not exchanging:
            break

lista1 = [1,3,4,7,9,0]
bsort(lista1)
print(lista1)