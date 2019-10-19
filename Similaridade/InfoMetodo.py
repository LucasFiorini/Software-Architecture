class InfoMetodo:
    vezes_chamado = 0
    nome_metodo = ''

    def __init__(self, nome_metodo):
        self.nome_metodo = nome_metodo
        self.vezes_chamado = 1
