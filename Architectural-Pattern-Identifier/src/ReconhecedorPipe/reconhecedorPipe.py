import ast

class Analisador(ast.NodeVisitor):
    chamadas = []
    tem_input = False
    tem_print = False
    tem_leitura_arquivo = False
    tem_escrita_arquivo = False

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
        if isinstance(chamada.func, ast.Attribute):
            if chamada.func.attr == "read":
                self.tem_leitura_arquivo = True
            elif chamada.func.attr == "write":
                self.tem_escrita_arquivo = True

        self.generic_visit(chamada)

    def limpar_atributos(self):
        self.chamadas = []
        self.tem_input = False
        self.tem_print = False
        self.tem_leitura_arquivo = False
        self.tem_escrita_arquivo = False


class ReconhecedorPipe:
    analisador = None
    arvore = None
    map_metodo_classe = {}
    map_classe_chamadas = {}
    filters = []
    pipes = []
    sinks = []
    pumps = []


    def __init__(self, caminho_arquivo):
        self.analisador = Analisador()
        with open(caminho_arquivo, "r") as codigo_analisado:
            self.arvore = ast.parse(codigo_analisado.read())
            #print(ast.dump(self.arvore))
        self.analisar()

    def analisar(self):
        for classe in self.arvore.body:
            if isinstance(classe, ast.ClassDef):
                self.mapear_classe_chamadas(classe)
                self.is_pipe(classe)
                self.is_sink(classe)
                for metodo in classe.body:
                    if isinstance(metodo, ast.FunctionDef):
                        self.map_metodo_classe[metodo.name] = classe.name
        self.is_pump()
        self.is_filter()

    def mapear_classe_chamadas(self, classe):
        self.analisador.limpar_atributos()
        self.analisador.visit(classe)
        lista_chamadas = self.analisador.chamadas
        self.map_classe_chamadas[classe.name] = lista_chamadas

    def is_pump(self):
        for classe in self.arvore.body:
            if isinstance(classe, ast.ClassDef):
                self.analisador.limpar_atributos()
                self.analisador.visit(classe)
                if self.analisador.tem_input and self.analisador.tem_print:
                    for metodo in self.map_classe_chamadas[classe.name]:
                        if self.map_metodo_classe[metodo] == 'Pipe':
                            self.pumps.append(classe.name)

    def is_pipe(self, classe):
        self.analisador.limpar_atributos()
        self.analisador.visit(classe)
        if self.analisador.tem_escrita_arquivo:
            self.pipes.append(classe.name)

    def is_sink(self,classe):
        self.analisador.limpar_atributos()
        self.analisador.visit(classe)
        if self.analisador.tem_print and not self.analisador.tem_input and self.analisador.tem_leitura_arquivo:
            self.sinks.append(classe.name)

    def is_filter(self):
        for classe in self.arvore.body:
            if isinstance(classe, ast.ClassDef):
                self.analisador.limpar_atributos()
                self.analisador.visit(classe)
                if not self.analisador.tem_input and not self.analisador.tem_print:
                    for metodo in self.map_classe_chamadas[classe.name]:
                        try:
                            if self.map_metodo_classe[metodo] == 'Pipe':
                                self.filters.append(classe.name)
                        except:
                            continue

a = ReconhecedorPipe("exemplos/" + "exemploPipe.py")
print("Pumps: " + str(a.pumps))
print("Pipes: " + str(a.pipes))
print("Sinks: " + str(a.sinks))
print("Filters: " + str(a.filters))