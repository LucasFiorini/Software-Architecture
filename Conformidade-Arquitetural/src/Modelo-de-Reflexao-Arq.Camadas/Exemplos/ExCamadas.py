class V1:
    def v11():
        input()
        print()
        B.b1()
        V2.v21()


class V2:
    def v21():
        input()
        print()
        X.x1()


class A:
    def a1():
        pass


class B:
    def b1():
        C.c1()
        X.x1()
        V2.v21()


class Qualquer:
    def oi():
        B.b1()


class X:
    def x1():
        C.c1()


class C:
    def c1():
        V2.v21()
