lista = []
total: float = 0.0

for i in range(4):
    lista.append(float(input(f"Digite a {i + 1}º Nota:")))
print(f" as notas são respectivamente:{lista}")
for i, v in enumerate(lista):
    total += v
print(f"A media de notas é: {total/len(lista)}")


