import ast

class Analisador(ast.NodeVisitor):
    atributos = []
    metodos = []

    def visit_Attribute(self, noh):
        if noh.value.id == "self":
            self.atributos.append(noh.attr)
        self.generic_visit(noh)

    def visit_FunctionDef(self, noh):
        self.metodos.append(noh.name)
        self.generic_visit(noh)

    def limpar_atributos(self):
        self.atributos = []
        self.metodos = []

def montar_classes(caminho):
    analisador = Analisador()
    lista_classes = []
    with open(caminho, "r") as codigo_analisado:
        arvore = ast.parse(codigo_analisado.read())
    for noh in arvore.body:
        if isinstance(noh, ast.ClassDef):
            classe = noh
            nova_classe = {"nome":classe.name}
            analisador.limpar_atributos()
            analisador.visit(classe)
            nova_classe["qnt_atributos"] = len(analisador.atributos)
            nova_classe["qnt_metodos"] = len(analisador.metodos)
            lista_classes.append(nova_classe)
    return lista_classes
