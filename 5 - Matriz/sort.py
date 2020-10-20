#[8,52,4,7,2,9]
lista1 = [1,4,5,6,7]
lista2 = [6,8,43,50,12]
lista3 = lista1 + lista2

print(lista3)

lista = []
for c in range(0,5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista... ')
    else:
        posicao = 0
        while posicao < len(lista):
            if n <= lista[posicao]:
                lista.insert(posicao, n)
                print(f'Adicionado na posição {posicao}')
                break
            posicao += 1
print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')