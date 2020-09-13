#Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo:
nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a Segunda nota: '))
media = (nota1 + nota2) / 2

if media >= 9.0:
    c = 'A'
elif media >= 7.5 and media < 9.0:
    c = 'B'
elif media >= 6.0 and media < 7.5:
    c = 'C'
elif media >= 4.0 and media < 6.0:
    c = 'D'
elif media >= 0 and media < 4.0:
    c = 'E'
if c in ("A","B","C"):
    resultado = "Aprovado!"
elif c in ("D", "E"):
    resultado = "Reprovado"

print('As notas P1: {} e P2 {}, são {} e voce foi {}'.format(nota1, nota2, c, resultado))
