class View:

    def __init__(self):
        print("informe o que deseja fazer: ")

    def digitar_opcao(self):
        print("digite o que deseja fazer")

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
