# Dicionário para agrupar participantes por tema
eventos = {}

# Entrada do número de participantes
n = int(input().strip())

# TODO: Crie um loop para armazenar participantes e seus temas:
for _ in range(n):
  linha = input().strip().title()

  posicao_espaco = linha.rfind(" ")

  participantes = linha[:posicao_espaco]
  tema = linha[posicao_espaco + 1:]

  if tema not in eventos:
    eventos[tema] = []

  eventos[tema].append(participantes)


# Exibe os grupos organizados
for tema, participantes in eventos.items():
  print(f"{tema}: {', '.join(participantes)}")