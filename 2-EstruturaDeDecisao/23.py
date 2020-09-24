#Faça um Programa que peça um número e informe se o número é inteiro ou decimal. Dica: utilize uma função de arredondamento.

numero = float(input("Digite o numero a verificar: "))

if round(numero) == numero:
    print("O numero é Inteiro!")
else:
    print("O numero é Decimal!")
