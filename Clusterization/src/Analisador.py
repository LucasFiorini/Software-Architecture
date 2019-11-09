import ast

class Analisador(ast.NodeVisitor):

    lista_metodos = []
    lista_chamadas = []

    def visit_FunctionDef(self, classe):
        self.lista_metodos.append(classe.name)
        self.generic_visit(classe)

    def visit_Call(self, classe):
        if isinstance(classe.func, ast.Attribute):
            self.lista_chamadas.append(classe.func.attr)
        self.generic_visit(classe)

    def limpar_atributos(self):
        self.lista_metodos = []
        self.lista_chamadas = []
