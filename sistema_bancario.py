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
        valor_deposito = float(input('Digite o valor a ser depositado: '))
        if valor_deposito > 0:
            extrato += f'R$ +{valor_deposito:,.2f}\n'
            saldo += valor_deposito
        else: print('Digite um valor valido para deposito')

    elif opcao == 's':
        valor_sacar = float(input('Digite o valor a ser sacado: '))

        limite_saque_atingido = LIMITE_SAQUES < 1
        saldo_insuficiente = valor_sacar > saldo
        valor_saque_superior_limite_diario = valor_sacar > LIMITE_POR_SAQUE

        if limite_saque_atingido:
            print('Número de saques já realizados atingiu o limite. Tente novamente amanhã.')
            
        elif saldo_insuficiente:
            print(f'Valor desejado do saque maior que o saldo em conta. Saldo atual: R$ {saldo:,.2f}')

        elif valor_saque_superior_limite_diario:
            print('Valor desejado superior ao limite por saque')

        elif valor_sacar > 0:
            extrato += f'R$ -{valor_sacar:,.2f}\n'
            saldo -= valor_sacar
            LIMITE_SAQUES = LIMITE_SAQUES - 1
        
        else:
            print('Valor informado para saque é invalido.')
                

    elif opcao == 'e':
        print(f"""
\n===== Extrato =====
{'Não foram realizadas movimentações' if not extrato else extrato}  
\n===== Saldo =====
{saldo:,.2f}
\n=================
""")

    elif opcao == 'q':
        print('Obrigado!')
        break

    else:
        print('Opção inválida, por favor selecionar a opção com a operação desejada.')