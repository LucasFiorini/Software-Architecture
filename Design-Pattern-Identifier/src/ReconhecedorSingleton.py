import ast

class ReconhecedorSingleton:
    lista_classes = []

    def __init__(self, arquivo):
        with open(arquivo, "r") as codigo_analisado:
            arvore = ast.parse(codigo_analisado.read())
            for classe in ast.walk(arvore):
                if isinstance(classe, ast.ClassDef):
                    self.lista_classes.append(classe)

    # Retorna True se a classe possui um atributo privado chamado instancia
    def possui_atributo_instancia(self, classe):
        for atribuicao in classe.body:
            if isinstance(atribuicao, ast.Assign):
                if atribuicao.targets[0].id == "__instancia":
                    return True
        return False

    # Retorna True e o nome da classe interna privada caso esta seja de mesmo
    # nome em relacao a classe externa
    def possui_classe_de_mesmo_nome(self, classe):
        for classe_interna in classe.body:
            if isinstance(classe_interna, ast.ClassDef):
                suposto_nome = "__" + classe.name
                if classe_interna.name == suposto_nome:
                    return True, classe_interna.name
        return False, ""

    # "ci" indica que este metodo eh utilizado pelo metodo
    # "possui_controle_de_instanciacao"
    def ci_verificacao_de_instancia_nula(self, metodo, nome_classe_interna):
        # Verifica a presenca da expressao:
        # "if not cls.__instancia:"
        for condicional in metodo.body:
            if isinstance(condicional, ast.If):
                if isinstance(condicional.test.op, ast.Not) and\
                        condicional.test.operand.attr == "__instancia":
                    if self.ci_instanciacao_de_nova_instancia(condicional, nome_classe_interna):
                        return True
        return False

    # "ci" indica que este metodo eh utilizado pelo metodo
    # "possui_controle_de_instanciacao"
    def ci_instanciacao_de_nova_instancia(self, condicional, nome_classe_interna):
        # Verifica a presenca da expressao:
        # "cls.__instancia = cls.__NomeClasse()", dentro da condicional
        for atribuicao in condicional.body:
            if isinstance(atribuicao, ast.Assign):
                if atribuicao.targets[0].attr == "__instancia" and\
                        atribuicao.value.func.attr == nome_classe_interna:
                    return True
        return False

    # "ci" indica que este metodo eh utilizado pelo metodo
    # "possui_controle_de_instanciacao"
    def ci_retorno_da_instancia(self, metodo):
        # Verifica a presenca da expressao:
        # "return cls.__instancia"
        for retorno in metodo.body:
            if isinstance(retorno, ast.Return):
                if retorno.value.attr == "__instancia":
                    return True
        return False

    # Verifica se a classe controla quantas instancias de si propria ela possui.
    # Faz uso dos metodos:
    #     ci_verificacao_de_instancia_nula
    #     ci_instanciacao_de_nova_instancia (indiretamente)
    #     ci_retorno_da_instancia
    def possui_controle_de_instanciacao(self, classe, nome_classe_interna):
        for metodo in classe.body:
            if isinstance(metodo, ast.FunctionDef):
                if metodo.name == "__new__":
                    # A sub_evidencia2 eh observada no interior do metodo
                    # ci_verificacao_de_instancia_nula, de maneira implicita
                    sub_evidencia1 = self.ci_verificacao_de_instancia_nula(metodo, nome_classe_interna)
                    sub_evidencia2 = self.ci_retorno_da_instancia(metodo)
                    if sub_evidencia1 and sub_evidencia2:
                        return True
        return False

    def reconhecer_singleton(self):
        for classe in self.lista_classes:
            evidencia1 = self.possui_atributo_instancia(classe)
            evidencia2, nome_classe_interna = self.possui_classe_de_mesmo_nome(classe)
            evidencia3 = self.possui_controle_de_instanciacao(classe, nome_classe_interna)
            if evidencia1 and evidencia2 and evidencia3:
                print("A classe", classe.name, "apresenta o padrao singleton.")
            else:
                pass