import ast

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
