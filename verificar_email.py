# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:
if " " in email:
  print("E-mail inválido")
elif email.startswith("@"):
  print("E-mail inválido")
elif "@gmail.com" in email or "@outlook.com" in email:
  print("E-mail válido")
  