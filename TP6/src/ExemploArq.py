class Interface:
    elementos_graficos = []

    def evento_cadastrar(self):
        nome = input("Digite seu nome: ")
        p = Pessoa(nome)
        self.elementos_graficos.append(p)
        self.atualizar()

    def atualizar(self):
        for elemento in self.elementos_graficos:
            print(elemento)
        print()


class Pessoa:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "O nome dessa pessoa eh "+self.nome


class Robo:
    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return "O nome desse robo eh "+self.nome


i = Interface()
i.evento_cadastrar()
i.evento_cadastrar()
