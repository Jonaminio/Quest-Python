
sair = 2
while sair == 2:
    print('{:-^60}\n< 1 > Somar 2 Numeros\n< 2 > Subtrair 2 Numeros\n< 3 > Multiplicar 2 Numeros\n< 4 > Dividir 2 Numeros\n'.format('-'))
    selecao = int(input('Digite a Opção desejada: \n{:-^60}\n'.format('-')))
    while selecao < 5:
        numero1 = int(input('Digite o Primeiro nuemro: '))
        numero2 = int(input('Digite o Segundo numero: '))
        if selecao == 1:
            print('A soma de {} com {} é: {}'.format(numero1, numero2, numero1 + numero2))
        if selecao == 2:
            print('A Subtração de {} com {} é {}'.format(numero1, numero2, numero1 - numero2))
        if selecao == 3:
            print('A Multiplicação de {} com {} é {}'.format(numero1, numero2, numero1 * numero2))
        if selecao == 4:
            print('A Divisão de {} com {} é {}'.format(numero1, numero2, numero1 / numero2))
        break
    sair = int(input('\n\nDigite 1 para Sair ou Digite 2 Para Reiniciar: '))
    if sair == 1:
        sair = 1
        break
    if sair == 2:
        sair = 2
    else:
        print('Digite  apenas 1 ou 2')
        sair = int(input('Digite 1 para Sair ou Digite 2 Para Reiniciar: '))