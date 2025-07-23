n = int(input().strip())

pacientes_urgentes = []
pacientes_comuns = []

for _ in range(n):
    nome, idade, status = input().strip().split(", ")
    idade = int(idade)
    paciente = (nome, idade, status)
    if status == "urgente":
        pacientes_urgentes.append(paciente)
    else:
        pacientes_comuns.append(paciente)

def ordenar_por_idade(p):
    return -p[1] # Aqui temos a separação: | p[0] = nome | p[1] = idade | p[2] = status |

pacientes_urgentes.sort(key=ordenar_por_idade)
pacientes_comuns.sort(key=ordenar_por_idade)

ordem_final = pacientes_urgentes + pacientes_comuns
# Exibe a ordem de atendimento
print("Ordem de Atendimento: " + ", ".join([p[0] for p in ordem_final]))