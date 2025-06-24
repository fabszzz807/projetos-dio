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
            extrato += f"Deposito: R${deposito:.2f} | "
            print(f"Saldo: {saldo:.0f}")

    elif opcao == "s":
        print("Saque")
        saque = float(input("Quanto voce quer sacar: "))
        if numero_saques < 3:
            if saque <= saldo:
                if saque <= limite:
                    numero_saques += 1
                    saldo -= saque
                    print(f"Saldo restante: {saldo}")
                    extrato += f"Saque: {saque:.2f} | "
                    print(numero_saques)
                else:
                    print("Maior que o limite")
            else:
                print("Saldo insuficiente")
        else:
            print("Limite de saques excedido")
    elif opcao == "e":
        print("Extrato")
        print(extrato)
    elif opcao == "q":
        break
    else:
        print("Operacao invalida, por favor selecione novamente a operacao desejada.")