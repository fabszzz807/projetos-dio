menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        deposito = float(input("Quanto voce quer depositar: "))
        if deposito < 0:
            print("Digite um valor positivo")
            continue
        else:
            saldo += deposito
            extrato += f"Deposito: R$ {deposito:.2f}\n"
            print(f"Saldo: R$ {saldo:.2f}")

    elif opcao == "s":
        print("Saque")
        saque = float(input("Quanto voce quer sacar: "))

        if saque > 0:
            if saque <= saldo:
                if numero_saques < LIMITE_SAQUES:
                    if saque <= limite:
                        numero_saques += 1
                        saldo -= saque
                        print(f"Saldo restante: R$ {saldo:.2f}")
                        extrato += f"Saque: R$ {saque:.2f}\n"
                    else:
                        print("Operacao falhou! O valor do saque excede o limite.")
                else:
                    print("Operacao falhou! Voce nao tem saldo suficiente.")
            else:
                print("Operacao falhou! Numero maximo de saques excedido.")
        else:
            print("Saque nao pode ser negativo")
    elif opcao == "e":
        print("\n============ Extrato ============")
        print("Nao foram realizadas movimentacoes." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("=================================")
    elif opcao == "q":
        break
    else:
        print("Operacao invalida, por favor selecione novamente a operacao desejada.")
