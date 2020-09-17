numero = int(input('Digite um numero inteiro positivo: '))
# exemplo: 4321
# 1 - Unidade (Numero: 1)
unidade = numero % 10 # 4321 % 10 == 1
# 2 - Dezena (Numero: 2)
numero = (numero - unidade) / 10 # (4321 - 1) == 4320 | (4320) / 10 == 432
dezena = numero % 10 # 432 % 10 == 2
# 3 - Centena (Numero: 3)
numero = (numero - dezena) / 10 # (432 - 2) == 430 | (430) /10 == 43
centena = numero % 10 # 43 % 10 == 3
# 4 - Milhar (Numero: 4)
numero = (numero - centena) / 10 # (43 - 3 == 40) | (40) / 10 == 4
milhar = numero

print(f'{round(milhar)} milhar(es) e {round(centena)} centena(s) e {round(dezena)} dezena(s) e {round(unidade)} unidade(s)')
