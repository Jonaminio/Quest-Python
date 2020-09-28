lista = []
consoantes = []

for i in range(10):
    lista.append(str(input(f"Digite a {i+1}º Letra a ser verificada: ")))
    if lista[i] not in 'aeiouAEIOU':
        consoantes.append(lista[i])

print(f"Voce digitou as seguintes letras: {lista}")
print("E as consoantes são:{} ".format(consoantes))