import ast

porcentagem_minima = 60

class InfoChamadas:
    nome_classe = ""
    lista_metodos_locais = []
    lista_metodos_externos = []

    def __init__(self,nome , lista_locais, lista_externos):
        self.nome_classe = nome
        self.lista_metodos_locais = lista_locais
        self.lista_metodos_externos = lista_externos


class ReconhecedorFacade:
    map_metodos_classes = {}
    lista_classes = []
    lista_chamadas_metodos = []

    # guarda na lista de classes todas as classes encontradas no codigo
    def __init__(self, arquivo):
        with open(arquivo, "r") as codigo_analisado:
            arvore = ast.parse(codigo_analisado.read())
            for classe in ast.walk(arvore):
                if isinstance(classe, ast.ClassDef):
                    self.lista_classes.append(classe)

    # Guarda em um map todos os metodos de todas as classes
    # a chave eh o nome da classe e o conteudo o nome dos metodos
    def reconhecer_metodos(self, classe):
        nome_classe = classe.name
        for metodo in classe.body:
            if isinstance(metodo, ast.FunctionDef):
                if nome_classe not in self.map_metodos_classes:
                    self.map_metodos_classes[nome_classe] = [metodo.name]
                else:
                    self.map_metodos_classes[nome_classe].append(metodo.name)

    def reconhecer_facade(self):
        for classe in self.lista_classes:
            self.reconhecer_metodos(classe)
        for classe in self.lista_classes:
            self.identifica_chamadas(classe)
        for obj in self.lista_chamadas_metodos:
            total = len(obj.lista_metodos_locais) + len(obj.lista_metodos_externos)
            if total > 0:
                if (100 * len(obj.lista_metodos_externos)) / total >= porcentagem_minima:
                    print("A classe " + obj.nome_classe + " apresenta o padrao facade")




    # Identifica chamadas de metodos dentro do corpo das classes guardadas
    # na lista de classes, onde a cada chamada uma classe eh analisada
    # Guarda na lista de chamadas de metodos infomracao sobre chamadas de metodos
    # de cada classe
    def identifica_chamadas(self, classe):
        lista_metodos_locais = []
        lista_metodos_externos = []
        nome_classe = classe.name
        for metodo in classe.body:
            if isinstance(metodo, ast.FunctionDef):
                for chamadas in metodo.body:
                    try:
                        nome_metodo = chamadas.value.func.attr
                        if self.verifica_nacionalidade(nome_metodo, nome_classe):
                            lista_metodos_externos.append(nome_metodo)
                        else:
                            lista_metodos_locais.append(nome_metodo)
                    except:
                        continue
        obj = InfoChamadas(nome_classe, lista_metodos_locais, lista_metodos_externos)
        self.lista_chamadas_metodos.append(obj)

    # Verifica no map se o metodo eh de outra classe
    def verifica_nacionalidade(self, nome_metodo, nome_classe):
        if nome_metodo in self.map_metodos_classes[nome_classe]:
            return False
        else:
            return True
