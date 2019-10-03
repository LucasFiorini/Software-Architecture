class View:

    def __init__(self):
        print("informe o que deseja fazer: ")

    def digitar_opcao(self):
        print("digite o que deseja fazer")
        opcao = input()

    def processa_opcao(self):
        Presenter.nome_model()
        Presenter.instanciar_n_classes(10)



class Presenter:

    def nome_model(self):
        #m = Model()
        return Model.getName()


    def instanciar_n_classes(qtd_classes):
        for i in range(qtd_classes):
            m = Model()


class Model:

    def __init__(self):
        print("instancia de Model")

    def getName(self):
        return "Model"


class Model2:

    def __init__(self):
        print("instancia de Model2")

    def getNames(self):
        return "Model2"


class Teste:
    def __init__(self):
        pass

    def faz_alguma_coisa(self):
        Presenter.instanciar_n_classes(10)


class V:

    def __init__(self):
        print("informe o que deseja fazer: ")

    def digitar_opcao(self):
        print("digite o que deseja fazer")
        opcao = input()

    def processa_opcao(self):
        P.nomeModel()
        P.instanciar(10)



class P:

    def nomeModel(self):
        m = M()
        return M.getNamez()


    def instanciar(qtd_classes):
        for i in range(qtd_classes):
            m = M()


class M:

    def __init__(self):
        print("instancia de Model")

    def getNamez(self):
        return "Model"



class Visao:

    def __init__(self):
        print("informe o que deseja fazer: ")

    def digitar_opcao(self):
        print("digite o que deseja fazer")
        opcao = input()

    def processa_opcao(self):
        Apresentador.nome_model()
        Apresentador.instanciar_n_classes(10)



class Apresentador:

    def nome_model(self):
        #m = Model()
        return Modelo.getName()


    def instanciar_n_classes(qtd_classes):
        for i in range(qtd_classes):
            m = Modelo()


class Modelo:

    def __init__(self):
        print("instancia de Model")

    def getName(self):
        return "Model"
