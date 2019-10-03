class View1:
    def v1(self):
        input()
        print()


class View2:
    def v2(self):
        input()
        print()


class Model:
    def __init__(self):
        pass

    def m1(self):
        pass


class Controller:
    def interagir_view(self):
        View1.v1()
        View2.v2()

    def interagir_model(self):
        Model.m1()


