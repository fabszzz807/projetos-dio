# Dicionário com os valores de desconto
descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

# Entrada do usuário
preco = float(input().strip())
cupom = input().strip().upper()

# TODO: Aplique o desconto se o cupom for válido:
if cupom in descontos:
  if cupom == "DESCONTO10":
    preco_final = preco - (preco * descontos["DESCONTO10"])
  elif cupom == "DESCONTO20":
    preco_final = preco - (preco * descontos["DESCONTO20"])
  else:
    preco_final = preco
else:
  print("Cupom invalido")
  
print(f'{preco_final:.2f}')