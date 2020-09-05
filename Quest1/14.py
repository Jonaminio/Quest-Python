max = 50
peso = float(input('Digite o peso do peixe: '))
if peso > max:
    print("Levou multa de {:.2f} R$".format((peso - max) * 4))
else:
    print('Sem Multas')
