saque = float(input("Digite o Valor que Queres sacar: "))

if saque >= 10.0 and saque <= 600.0:
    #de 200 pra diferenciar
    #duzentos = saque // 200
    #saque = saque % 200
    #print(saque, duzentos)
    cem = saque // 100
    saque = saque % 100

    cinquenta = saque // 50
    saque = saque % 50

    dez = saque // 10
    saque = saque % 10

    cinco = saque // 5
    saque = saque % 5

    #print('{} de 200 R$'.format(duzentos))
    print('{:.0f} de 100 R$'.format(cem))
    print('{:.0f} de  50 R$'.format(cinquenta))
    print('{:.0f} de  10 R$'.format(dez))
    print('{:.0f} de   5 R$'.format(cinco))
    print('{:.0f} de   1 R$'.format(saque))
else:
    print("O Valor não está entre 10 R$ e 600 R$")

