#aça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
#Observando os termos no plural a colocação do "e", da vírgula entre outros.

numero = int(input('Digite um numero inteiro positivo: '))
if numero <= 1000:
# Extraindo a unidade ex 321 == 1
    unidade = numero % 10

# Tirando a unidade  311 = (321 - 1) ==> 320 ==> 320 / 10 = 32
    numero = (numero - unidade) / 10

# Tirando a dezena 32 % 10 ==> 2
    dezena = numero % 10

# Eliminando a dezena do número original, fica a centena 32 - 2 ==> 30 ==> 30/10 == 3
    numero = (numero - dezena) / 10
    centena = numero

    print(f'{round(centena)} centena(s) e {round(dezena)} dezena(s) e {round(unidade)} unidade(s)')

else:
    print('é maior que 1000')
