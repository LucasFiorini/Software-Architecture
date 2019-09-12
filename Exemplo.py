class Carro():
    placa = "ABC-1234"

    def __init__(self, numero_portas):
        self.__numero_portas = numero_portas

    def rodar_chave(self):
        self.__ligar_motor()

    def __ligar_motor(self):
        pass

    def __desligar_motor(self):
        pass

    def __dormir(self):
        pass

class Catioro():

    def __init__(self, numero_patas):
        self.__numero_patas = numero_patas

    def latir(self):
        self.__avancar()

    def __avancar(self):
        pass

    def __dormir(self):
        pass


class Bus():

    def __init__(self, numero_patas):
        self.__numero_patas = numero_patas

    def latir(self):
        self.__avancar()

    def __avancar(self):
        pass

    def __dormir(self):
        pass


def main():
    c1 = Carro(2)
    c1.rodar_chave()
    c3 = Catioro(4)
    c3.__dormir()

if __name__ == "__main__":
    main()
