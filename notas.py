# Fatiamento de string
text = "python"

text2 = text[0:3]

print(text2)


# Funcão enumerate
carros = ["gol", "celta", "palio"]

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")


# Filtro versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)


# Filtro versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]


# Modificando valores versão 1
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = []

for numero in numeros:
    quadrado.append(numero ** 2)


# Modificando valores versão 2
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero ** 2 for numero in numeros]


### Métodos da classe list

# append
lista = []

lista.append(1)
lista.append("Python")
lista.append([1, 33, 64])

print(lista)


# clear
lista = [1, 33, "Python", "Celta"]

lista.clear()

print(lista)


# copy
lista = [2, 45, 60, "Python"]

l2 = lista.copy()


# count
lista = ["Vermelho", "Azul", "Verde", "Azul"]

lista.count("Vermelho") # 1
lista.count("Azul") # 2
lista.count("Verde") # 1


# extend
lista = ["python", "js", "c"]

lista.extend(["java", "csharp"])

print(lista) # ["python", "js", "c", "java", "csharp"]


# index
lista = ["python", "java", "c", "js", "java", "csharp"]

lista.index("python") # 0
lista.index("js") # 3


# pop
lista = ["python", 45, 6, "js", "csharp"]

lista.pop() # "csharp"
lista.pop() # "js"
lista.pop(0) # "python"


# remove
lista = ["python", "java", "c", "js", "java"]

lista.remove("java") # "java"


# reverse
lista = ["python", "java", "c", "js", "java"]

lista.reverse() # ["java", "js", "c", "java", "python"]


# sort
lista = ["python", "java", "c", "js", "java"]

lista.sort() # ["c", "java", "java", "js", "python"]


# len
lista = ["python", 45, 6, "js", "csharp"]

len(lista) # 5


### Tupla
frutas = ("laranja", "pera", "uva")

letras = tuple("python")

numeros = tuple([1, 2, 3, 4])

pais = ("Brasil",)

frutas[0] # laranja
frutas[2] # uva

# Tuplas aninhadas
matriz = (
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c"),
)

matriz[0] # (1, "a", 2)
matriz[0][0] # 1
matriz [0][-1] # 2
matriz [-1][-1] # "c"

# Fatiamento
tupla = ("p", "y", "t", "h", "o", "n",)

tupla[2:] # ("t", "h", "o", "n")
tupla[:2] # ("p", "y")


### Conjunto (set)
set([1, 2, 3, 1, 3, 4]) # {1, 2, 3, 4}

set("abacaxi") # {"b", "a", "c", "x", "i"}

set(("palio", "gol", "celta", "palio")) # {"gol", "celta", "palio"}

linguagens = {"python", "java", "python"} # {"java", "python"}


# Transformando conjunto em lista
numeros = {1, 2, 4, 3, 2}

numeros = list(numeros)

numeros[0]


# Iterando conjutos
carros = {"gol", "palio", "kwid"}

for carro in carros:
	print(carro)
     

# Métodos da classe set

# union
conjunto_a = {1, 2}
conjunto_b = {3, 4}

conjunto_a.union(conjunto_b) # {1, 2, 3, 4}


# intersection
conjunto_c = {1, 2, 3}
conjunto_d = {2, 3, 4}

conjunto_c.intersection(conjunto_d) # {2, 3}


# difference
conjunto_c.difference(conjunto_d) # {1}
conjunto_d.difference(conjunto_c) # {4}


# symmetric difference
conjunto_c.symmetric_difference(conjunto_d) # {1, 4}


# issubset
conjunto_e = {1, 2, 3}
conjunto_f = {4, 2, 5, 1, 7, 3}

conjunto_e.issubset(conjunto_f) # True
conjunto_f.issubset(conjunto_e) # False


### Dicionários
pessoa = {"nome": "Fabricio", "idade": 24}

pessoa = dict(nome="Fabricio", idade=24)

pessoa["telefone"] = "3333-1234" # {"nome": "Fabricio", "idade": 24, "telefone": "3333-1234"}

# Exemplo
dados = {"nome": "Fabricio", "idade": 24, "telefone": "3333-1234"}

dados["nome"] # "Fabricio"
dados["idade"] # 24
dados["telefone"] # "3333-1234"


# items
contatos = {
     "fabricio@gmail.com": {"nome": "Fabricio", "telefone": "3333-2221"},
     "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3443-2121"}
}

for chave, valor in contatos.items():
     print(chave, valor)

     
### Funcões



