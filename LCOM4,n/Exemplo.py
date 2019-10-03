class Exemplo():
    x = None
    y = 20
    z = None
    __w = 22

    def __init__(self, qualquer):
        self.x = qualquer
        pass

    def a(self):
        return self.x + self.y

    def __b(self):
        self.x = self.x + 10000


    def d(self):
        return self.z


    def e(self):
        pass

    def getW(self):
        return self.__w
