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
    def interagirview(self):
        View1.v1()
        View2.v2()

    def interagirmodel(self):
        Model.m1()



class V:
    def v(self):
        input()
        print()


class M:
    def __init__(self):
        pass

    def m(self):
        pass


class C:
    def interagir_view(self):
        V.v()
        V.v()

    def interagir_model(self):
        M.m()
