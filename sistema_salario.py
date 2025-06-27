salario_bruto = float(input("Salario bruto: "))
adicional_beneficios = float(input("Beneficios: "))
aliquota = 0

if salario_bruto >= 0 and salario_bruto <= 1100:
    aliquota = salario_bruto * 0.05
elif salario_bruto > 1100 and salario_bruto <= 2500:
    aliquota = salario_bruto * 0.1
elif salario_bruto > 2500:
    aliquota = salario_bruto * 0.15
else:
    print("Valor invalido")

salario_total = (salario_bruto - aliquota) + adicional_beneficios

print(f"Salario final: R$ {salario_total:.2f}")