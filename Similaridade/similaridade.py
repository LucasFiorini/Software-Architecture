import ast

class Info_Class:
    qtd_conditional = 0
    qtd_loop = 0
    qtd_print = 0
    qtd_input = 0
    qtd_open = 0
    qtd_try = 0
    metodos_externos = []

    #def __init__(self, lista_atributos):



class InfoMetodo:
    vezes_chamado = 0
    nome_metodo = ''



class Similaridade:
    arvore = None
    map_classe_metodos = {}
    analisador = None

    def __init__(self, caminho_arquivo):
        with open(caminho_arquivo, "r") as codigo_analisado:
            self.arvore = ast.parse(codigo_analisado.read())
            #print(ast.dump(self.arvore))
            self.analisador = Analisador()
        self.explorar_arvore()

    def explorar_arvore(self):
        for classe in self.arvore.body:
            if isinstance(classe, ast.ClassDef):
                self.analisador.visit(classe)
                self.map_classe_metodos[classe.name] =  self.analisador.get_list_metodos()
                print("a classe " + classe.name  + " possui " + str(self.analisador.qtd_conditional) + " operadores condicionais")
                print("a classe " + classe.name  + " possui " + str(self.analisador.qtd_loop) + " operadores de repeticao")
                print("a classe " + classe.name  + " possui " + str(self.analisador.qtd_print) + " prints")
                print("a classe " + classe.name  + " possui " + str(self.analisador.qtd_input) + " inputs")
                print("a classe " + classe.name  + " possui " + str(self.analisador.qtd_open) + " opens")
                print("a classe " + classe.name + " possui " + str(self.analisador.qtd_try) + " opetadores de try")
                # self.filter_methods()
                self.analisador.clear_list()


    # def filter_methods(self):
    #     for


class Analisador(ast.NodeVisitor):
    lista_metodos = []
    lista_chamadas = []
    qtd_conditional = 0
    qtd_loop = 0
    qtd_print = 0
    qtd_input = 0
    qtd_open = 0
    qtd_try = 0

    def visit_If(self, classe):
        self.qtd_conditional += 1

    def visit_For(self, classe):
        self.qtd_loop += 1

    def visit_Try(self, classe):
        self.qtd_try += 1

    def visit_While(self, classe):
        self.qtd_loop += 1

    def visit_FunctionDef(self, classe):
        self.lista_metodos.append(classe.name)
        self.generic_visit(classe)

    def visit_Call(self, classe):
        if isinstance(classe.func, ast.Attribute):
            self.lista_chamadas.append(classe.func.attr)

        if isinstance(classe.func, ast.Name):
            if classe.func.id == "input":
                self.qtd_input += 1
            elif classe.func.id == "print":
                self.qtd_print += 1
            elif classe.func.id == "open":
                self.qtd_open += 1
        self.generic_visit(classe)

    def get_list_metodos(self):
        return self.lista_metodos


    def clear_list(self):
        self.lista_metodos = []
        self.qtd_conditional = 0
        self.qtd_loop = 0
        self.qtd_input = 0
        self.qtd_print = 0
        self.qtd_open = 0
        self.qtd_try = 0
        self.lista_chamadas = []


g = Similaridade("exemplo.py")
print(g.map_classe_metodos)






