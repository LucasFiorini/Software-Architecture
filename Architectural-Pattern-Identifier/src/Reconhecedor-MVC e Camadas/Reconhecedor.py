import ast

class Analisador(ast.NodeVisitor):
    chamadas = []
    tem_input = False
    tem_print = False

    def visit_Call(self, chamada):
        # Guarda chamadas de metodos
        if isinstance(chamada.func, ast.Attribute):
            self.chamadas.append(chamada.func.attr)
        # Reconhece inputs e prints
        if isinstance(chamada.func, ast.Name):
            if chamada.func.id == "input":
                self.tem_input = True
            elif chamada.func.id == "print":
                self.tem_print = True
        self.generic_visit(chamada)

    def limpar_atributos(self):
        self.chamadas = []
        self.tem_input = False
        self.tem_print = False


class Reconhecedor():
    arvore = None
    analisador = None
    map_metodo_classe = {}
    map_classe_chamadas = {}
    map_relacionamentos = {}
    views = []

    def __init__(self, caminho_arquivo):
        self.analisador = Analisador()
        with open(caminho_arquivo, "r") as codigo_analisado:
            self.arvore = ast.parse(codigo_analisado.read())
        self.analisar()
        self.reconhecer_relacionamentos()

    # Mapea cada nome de classe a suas respectivas chamadas de metodos;
    # Reconhce classes que sao views;
    # Mapea cada nome de metodo a sua respectiva classe "dona";
    def analisar(self):
        for classe in self.arvore.body:
            if isinstance(classe, ast.ClassDef):
                self.mapear_classe_chamadas(classe)
                self.verificar_se_eh_view(classe)
                for metodo in classe.body:
                    if isinstance(metodo, ast.FunctionDef):
                        if metodo.name != "__init__":
                            self.map_metodo_classe[metodo.name] = classe.name

    def mapear_classe_chamadas(self, classe):
        self.analisador.limpar_atributos()
        self.analisador.visit(classe)
        lista_chamadas = self.analisador.chamadas
        self.map_classe_chamadas[classe.name] = lista_chamadas

    def verificar_se_eh_view(self, classe):
        self.analisador.limpar_atributos()
        self.analisador.visit(classe)
        if self.analisador.tem_input and self.analisador.tem_print:
            self.views.append(classe.name)

    def reconhecer_relacionamentos(self):
        for classe in self.map_classe_chamadas.keys():
            self.map_relacionamentos[classe] = []
            for chamada in self.map_classe_chamadas[classe]:
                classe_dona = self.map_metodo_classe[chamada]
                if classe_dona not in self.map_relacionamentos[classe]:
                    # Ignora classe chamando metodos proprios
                    if classe != classe_dona:
                        self.map_relacionamentos[classe].append(classe_dona)

#
