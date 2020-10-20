nome_completo: str = 'Jonas Alves dos Santos Herminio'
idade: int = 25
sexo: str = 'Masculino'
data_nascimento: str = '18/07/1995'
altura: float = 1.80
peso: float = 70
pe: float = 42.0

lista_de_disciplinas = ['Pyton','Java','Economia']

dicionario = {
'nome_completo': 'Jonas Alves dos Santos Herminio',
'idade': '25',
'sexo': 'masculino',
'datanascimento': '18 de julho',
'altura': '1.80',
'peso': '70',
'pe': '42.0'
}

salario: float = 100.000

print(f"{nome_completo} Variavel {type(nome_completo)}")
print(f"{idade} Variavel {type(idade)}")
print(f"{sexo} Variavel {type(sexo)}")
print(f"{data_nascimento} Variavel {type(data_nascimento)}")
print(f"{altura} Variavel {type(altura)}")
print(f"{peso} Variavel {type(peso)}")
print(f"{pe} Variavel {type(pe)}")
print(dicionario,type(dicionario))
print(lista_de_disciplinas,type(lista_de_disciplinas))
print(salario,type(salario))