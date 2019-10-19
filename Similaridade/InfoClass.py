class InfoClass:
    name = ''
    qtd_conditional = 0
    qtd_loop = 0
    qtd_print = 0
    qtd_input = 0
    qtd_open = 0
    qtd_try = 0
    metodos_externos = []

    # Constroi o objeto com base em duas listas
    def __init__(self, name, lista_atributos, lista_metodos):
        self.name = name
        self.qtd_conditional = lista_atributos[0]
        self.qtd_loop = lista_atributos[0]
        self.qtd_print = lista_atributos[1]
        self.qtd_input = lista_atributos[2]
        self.qtd_open = lista_atributos[3]
        self.qtd_try = lista_atributos[4]
        self.metodos_externos = lista_metodos
