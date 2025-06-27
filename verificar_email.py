# Entrada do usuário
email = input().strip()

# TODO: Verifique as regras do e-mail:
if "@gmail.com" in email or "@outlook.com" in email:
  print("E-mail válido")
elif " " in email:
  print("E-mail inválido")
elif email.startswith("@"):
  print("E-mail inválido")
else:
  print("E-mail válido")
  