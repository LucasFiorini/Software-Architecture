import ast
from InfoClass import InfoClass
from InfoMetodo import InfoMetodo
from Analisador import Analisador
from Util import Util

class Similaridade:

    arvore = None
    map_classe_metodos = {}
    analisador = None
    lista_info_classes = []

    def __init__(self, caminho_arquivo):
        with open(caminho_arquivo, "r") as codigo_analisado:
            self.arvore = ast.parse(codigo_analisado.read())
#            print(ast.dump(self.arvore))
            self.analisador = Analisador()
        self.explorar_arvore()
        self.filtrar_metodos()

    # Retira metodos internos da lista de chamadas e contabiliza o numero de chamadas de cada um
    def filtrar_metodos(self):
        for classe in self.lista_info_classes:
            lista_filtrada = []
            for metodo in classe.metodos_externos:
                if self.eh_externo(metodo, classe.name):
                    if not Util.find(metodo, lista_filtrada):
                        novo_metodo = InfoMetodo(metodo)
                        lista_filtrada.append(novo_metodo)
                    else:
                        lista_filtrada[Util.encontra_indice(metodo, lista_filtrada)].vezes_chamado += 1
            classe.metodos_externos = lista_filtrada

    # Verifica se o metodos eh interno ou externo a uma classe
    def eh_externo(self, nome_metodo, nome_classe):
        if nome_metodo not in self.map_classe_metodos[nome_classe]:
            return True
        return False

    # Faz varredeura de todas as classes em uma arvore
    # Guarda numero de if, try, open etc e constroi um objeto do tipo InfoClass
    def explorar_arvore(self):
        lista_aux = []
        for classe in self.arvore.body:
            if isinstance(classe, ast.ClassDef):
                self.analisador.visit(classe)
                self.map_classe_metodos[classe.name] = self.analisador.get_list_metodos()
                lista_aux.append(self.analisador.qtd_conditional)
                lista_aux.append(self.analisador.qtd_loop)
                lista_aux.append(self.analisador.qtd_print)
                lista_aux.append(self.analisador.qtd_input)
                lista_aux.append(self.analisador.qtd_open)
                lista_aux.append(self.analisador.qtd_try)
                i = InfoClass(classe.name, lista_aux, self.analisador.lista_chamadas)
                self.lista_info_classes.append(i)
                self.analisador.clear_list()
