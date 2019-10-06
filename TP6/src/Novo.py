class Interface:
    elementos_graficos = []

    def evento_cadastrar(self):
        nome = input('Digite seu nome: ')
        Controller.procedimento_0(self, nome)

    def atualizar(self):
        for elemento in self.elementos_graficos:
            print(elemento)
        print()


class Pessoa:

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return 'O nome dessa pessoa eh ' + self.nome


class Robo:

    def __init__(self, nome):
        self.nome = nome

    def __str__(self):
        return 'O nome desse robo eh ' + self.nome


class Controller:

    def procedimento_0(view, nome):
        p = Pessoa(nome)
        view.elementos_graficos.append(p)
        view.atualizar()


i = Interface()
i.evento_cadastrar()
i.evento_cadastrar()
