salario_bruto = float(input("Salario bruto: "))
adicional_beneficios = float(input("Beneficios: "))
valor_imposto = 0

if salario_bruto >= 0 and salario_bruto <= 1100:
    valor_imposto = salario_bruto * 0.05
elif salario_bruto > 1100 and salario_bruto <= 2500:
    valor_imposto = salario_bruto * 0.1
elif salario_bruto > 2500:
    valor_imposto = salario_bruto * 0.15
else:
    print("Valor invalido")

salario_total = (salario_bruto - valor_imposto) + adicional_beneficios

print(f"Salario final: R$ {salario_total:.2f}")