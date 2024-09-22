menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""

saldo = 0
LIMITE_POR_SAQUE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        print('depositar')

    elif opcao == 's':
        print('sacar')

    elif opcao == 'e':
        print('extrato')

    elif opcao == 'q':
        print('Obrigado!')
        break

    else:
        print('Opção inválida, por favor selecionar a opção com a operação desejada.')