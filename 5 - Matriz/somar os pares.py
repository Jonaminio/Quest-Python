somavalorespares = 0
somavalorescoluna = 0
i = 0
maiorvalor = 0
matriz = [[0,0,0],[0,0,0],[0,0,0]]
for linha in range(0,3):
    for coluna in range(0,3):
        matriz[linha][coluna] = int(input(f'Digite um valor para a [{linha},{coluna}]: '))
print('-='*30)
for linha in range(0, 3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
        if matriz[linha][coluna] % 2 == 0:
            somavalorespares += matriz[linha][coluna]
    print()
print('-='*30)
print(f'A Soma dos valores pares é {somavalorespares}')
print('-='*30)
for linha in range(0,3):
    somavalorescoluna += matriz[linha][i]
print(f'A Soma dos valores da Terceira Coluna é: {somavalorescoluna}')
print('-='*30)
for coluna in range(0,3):
    if coluna == 0:
        maiorvalor = matriz[1][coluna]
    elif matriz[1][coluna] > maiorvalor:
        maiorvalor = matriz[1][coluna]
print(f'O Maior valor da segunda linha é: {maiorvalor}')