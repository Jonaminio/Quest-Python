def contaEmpresa(valorDeposito):
    return valorDeposito


def pagarFuncionario(valorPagamento, saldo):
    if valorPagamento <= contaEmpresa(valorDeposito):
        print("O valor foi depositado para o funcionário.")
        return pagarFuncionario(valorPagamento) - valorPagamento
    else:
        return "Não foi possível realizar o depósito. Saldo insuficiente."


escolha = 0
saldo = 0

#### Programa Principal ######
while (escolha != 3):
    print("""\nBEM VINDO A EMPRESA UMBRELLA
  Digite a função desejada
  1- Empresa
  2- Funcionário
  3- Sair""")

    escolha = int(input("Digite a escolha desejada: "))

    if (escolha == 1):
        print("""\nDigite a escolha desejada
    1- Depositar dinheiro
    2- Pagar funcionário""")

        escolhaEmpresa = int(input("Digite a escolha desejada: "))

        if (escolhaEmpresa == 1):
            valorDeposito = float(input("\nDigite qual o valor será depositado para a empresa:  "))
            saldo += contaEmpresa(valorDeposito)
            print(f'O valor depositado na conta foi de: {valorDeposito}')
            print(f"A conta da empresa possui o valor de: {saldo}")

        if (escolhaEmpresa == 2):
            valorPagamento = float(input("Digite qual o valor do depósito para o funcionário: "))

            print(f"Resultado da operação:\n{pagarFuncionario(valorPagamento)}")

            print(f"A conta da empresa possui o valor de: {contaEmpresa(valorDeposito)}")
    if (escolha == 2):
        print("""\nDigite a escolha desejada
    1- Pagar Funcionário"""

        # -------- FIM ---------- #