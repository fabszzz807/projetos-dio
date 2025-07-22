'''João tem uma bicicletaria e gostaria de registrar as vendas de suas bicicletas.
Crie um programa onde João informe: cor, modelo, ano e valor da bicicleta vendida.
Uma bicicleta pode: buzinar, parar e correr. Adicione esses comportamentos.'''

class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("bibi")

    def parar(self):
        print("parado")

    def correr(self):
        print("correndo")

cor = input("Informe a cor da bicicleta: ").strip().title()
modelo = input("Informe o modelo da bicicleta: ").strip().title()
ano = input("Informe o ano da bicicleta: ").strip().title()
valor = float(input("Informe o valor da bicicleta: ").strip().title())

bicicleta_1 = Bicicleta("Amarelo", "Bianchi", "2015", 2000)
bicicleta_2 = Bicicleta("Azul", "BMX", "2024", 1500)
bicicleta_3 = Bicicleta(cor, modelo, ano, valor)

def registrar_bicleta(bicicleta):
    print(f"Cor: {bicicleta.cor}\nModelo: {bicicleta.modelo}\nAno: {bicicleta.ano}\nValor: R${bicicleta.valor:.2f}\n")

registrar_bicleta(bicicleta_1)
registrar_bicleta(bicicleta_2)
registrar_bicleta(bicicleta_3)