def dobro(lista):
    posisao = 0
    while posisao < len(lista):
        lista[posisao] *=2
        posisao +=1
    print(lista)

dobro([1,2,3,4])