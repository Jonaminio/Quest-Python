altura_pai = float(input("Digite a Altura do seu pai em cm: "))
altura_mae = float(input("Digite a Altura da sua mãe em cm: "))
altura = float(input("Digite a sua Altura em cm: "))

m = ((altura_pai + altura_mae + 12.5) / 2)
f = ((altura_pai + altura_mae - 12.5) / 2)

print("cálculo para determinar a média de altura final de um indivíduo:")
print(f"se Homem sua altura será: {m}\n se Mulher sua altura será: {f} ")
print(f"sua altura estará entre: {m - 6.25} e {m + 6.25}")
print(f"A sua altura atual é: {altura}")