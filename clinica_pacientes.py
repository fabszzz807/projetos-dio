# Entrada do número de pacientes
n = int(input().strip())

# Lista para armazenar pacientes
pacientes = []

# Loop para entrada de dados
for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    pacientes.append((nome, idade, status))

# TODO: Ordene por prioridade: urgente > idosos > demais:
pacientes.sort(key=lambda p: (p[2] != "urgente", p[1] < 60, -p[1]))
# TODO: Exiba a ordem de atendimento com título e vírgulas:
print("Ordem de Atendimento:", ", ".join([p[0] for p in pacientes]))