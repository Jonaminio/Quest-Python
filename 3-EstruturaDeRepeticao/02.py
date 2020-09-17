#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
while True:
    nome = input('Digite o nome: ')
    senha = input('Digite a senha: ')
    if nome == senha:
        print('ERRO: São iguais digite novamente')
    else:
        break

