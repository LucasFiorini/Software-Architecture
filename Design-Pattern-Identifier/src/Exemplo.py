import six
import abc

# Classe abstrata
@six.add_metaclass(abc.ABCMeta)
class PizzaAbstrata():
    def auto_declaracao(self):
        pass


class PizzaConcreta(PizzaAbstrata):
    # Override
    def auto_declaracao(self):
        print("Eu sou uma massa de pizza!")


# Classe abstrata
@six.add_metaclass(abc.ABCMeta)
class DecoratorPizza(PizzaAbstrata):
    instancia_decorada = None

    def __init__(self, pizza):
        self.instancia_decorada = pizza

    # Override
    def auto_declaracao(self):
        self.instancia_decorada.auto_declaracao()


class Molho(DecoratorPizza):
    def __init__(self, pizza):
        DecoratorPizza.__init__(self, pizza)

    def auto_declaracao(self):
        self.instancia_decorada.auto_declaracao()
        print("Eu tenho molho!")


class Queijo(DecoratorPizza):
    def __init__(self, pizza):
        DecoratorPizza.__init__(self, pizza)

    def auto_declaracao(self):
        self.instancia_decorada.auto_declaracao()
        print("Eu tenho queijo!")


class Cpu:
    def pipeline(self):
        print("pipelining")


class Memory:
    def IO(self):
        print("Sending values")


class Disk:
    def Read(self):
        print("Reading data")


class ComputerFacade:
    def startComputer(self):
        Disk.Read()
        Memory.IO()
        Cpu.pipeline()

    def startProgram(self):
        Disk.Read()
        Cpu.pipeline()
        self.startComputer()


class A():
    __instancia = None

    class __A():
        def __init__(self, palavra):
            self.palavra = palavra

    def __new__(cls, palavra):
        if not cls.__instancia:
            cls.__instancia = cls.__A(palavra)
        return cls.__instancia


class B():
    __instancia = None

    class __B():
        def __init__(self, palavra):
            self.palavra = palavra

    def __new__(cls, palavra):
        return cls.__instancia


class Teste:
    __instancia = None

    class __Teste:
        def __init__(self, palavra):
            self.palavra = palavra

    def __new__(cls, palavra):
        pass
