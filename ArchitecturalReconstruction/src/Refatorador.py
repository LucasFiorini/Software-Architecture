import ast
import astor

class Refatorador():
    def __init__(self, arquivo):
        with open(arquivo, "r") as codigo_analisado:
            self.arvore = ast.parse(codigo_analisado.read())

    def injetar_metodo(self, nome_classe):
        for classe in self.arvore.body:
            if isinstance(classe, ast.ClassDef):
                if classe.name == nome_classe:
                    classe.body.append(self.metodo_deslocado)

    def remover_metodo(self, nome_metodo, nome_classe):
        for classe in self.arvore.body:
            if isinstance(classe, ast.ClassDef):
                if classe.name == nome_classe:
                    for metodo in classe.body:
                        if isinstance(metodo, ast.FunctionDef):
                            if metodo.name == nome_metodo:
                                self.metodo_deslocado = metodo
                                classe.body.remove(metodo)
                                # Nao deixa a classe vazia
                                if classe.body == []:
                                    classe.body.append(ast.Pass)

    def escrever_novo_codigo_no_arquivo(self, caminho_arquivo):
        novo_codigo = astor.to_source(self.arvore)
        arquivo = open(caminho_arquivo, "w")
        arquivo.writelines(novo_codigo)
