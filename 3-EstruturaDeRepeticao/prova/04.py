lista_de_disciplinas = []

nome_completo: str = 'Jonas Alves dos Santos Herminio'
idade: int = 25
sexo: str = 'Masculino'
data_nascimento: str = '18/07/1995'
altura: float = 1.80
peso: float = 70
pe: float = 42.0

while True:
    lista_de_disciplinas.append(input(f"Digite a Diciplina preferida: "))
    resp = str(input("Queres continuar a adicionar? [S] = para sim e [N] para não: "))
    if resp == 'N' or resp == 'n':
        break
for i in range(len(lista_de_disciplinas)):
    print(f"- {lista_de_disciplinas[i]}")
