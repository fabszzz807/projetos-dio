class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("auau")

    def __del__(self):
        print("Removendo a instância da classe.")

c = Cachorro("Marquinhos", "Caramelo")
c.latir()

del c

c.latir()