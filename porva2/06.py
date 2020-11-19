def calcula(combustivel, percurso, pessoas):
    i = 0
    i = percurso / pessoas
    print(f"O Combustivel é {i}")


while True:
    print("Digite 1 para inserir o combustível em litros no avião")
    print("Digite 2 para informar o percurso percorrido em Km")
    print("Digite 3 para informar a quantidade de pessoas da aeronave.")
    print("Digite 0 para Sair\n.")
    q = int(input("Digite a opção desejada: "))

    if q == 1:
        litros = float(input("digite o combustivel em litros"))
    elif q == 2:
        percurso = float(input("digite o percurso percorrido em Km"))
    elif q == 3:
        pessoas = int(input("quantidade de pessoas da aeronave"))
    else:
        print("Digite uma opção válida, saindo")
        break

calcula(litros, percurso, pessoas)

