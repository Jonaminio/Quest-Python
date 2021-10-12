def valorPagamento(valorp, atraso):
    if atraso < 1:
        valor = valorp
        print(valor)
        return valor
    else:
        valor = (valorp + valorp * 0.03 + 0.01 * atraso)
        print(valor)
        return valor


valor = []
vpago = 0
atraso = 0
quantidadepagamento = 0
valortotal = 0

while True:
    quantidadepagamento += 1
    vpago = float(input('digite o valor da prestacao? '))
    atraso = int(input('digite dias em atraso:'))
    if vpago == 0:
        break
    valor.append(valorPagamento(vpago, atraso))

quantidadepagamento -= 1
for i in range(quantidadepagamento):
    valortotal += valor[i]

print(f'foram pagas {quantidadepagamento} prestacoes no valor: {valor}')
print(f'Valor total de prestacoes pagas: {valortotal}')


