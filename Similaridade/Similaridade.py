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
    a = []
    b = []
    c = []
    d = []

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
    # Constroi objetos do tipo InfoClass
    def explorar_arvore(self):
        for classe in self.arvore.body:
            if isinstance(classe, ast.ClassDef):
                self.analisador.visit(classe)
                self.map_classe_metodos[classe.name] = self.analisador.lista_metodos
                i = InfoClass(classe.name, self.analisador.lista_chamadas)
                self.lista_info_classes.append(i)
                self.analisador.limpar_atributos()

    def calcular_a_b_c_d(self, nome_classe_1, nome_classe_2):
        a = 0
        b = 0
        c = 0
        d = 0
        chamadas_todas_classes = []
        chamadas_classe_1 = None
        chamadas_classe_2 = None
        for ic in self.lista_info_classes:
            if ic.name == nome_classe_1:
                chamadas_classe_1 = []
                for im in ic.metodos_externos:
                    chamadas_classe_1.append(im.nome_metodo)
            elif ic.name == nome_classe_2:
                chamadas_classe_2 = []
                for im in ic.metodos_externos:
                    chamadas_classe_2.append(im.nome_metodo)
            for met in ic.metodos_externos:
                if met.nome_metodo not in chamadas_todas_classes:
                    chamadas_todas_classes.append(met.nome_metodo)
        if chamadas_classe_1 == None or chamadas_classe_2 == None:
            return False
        for met in chamadas_todas_classes:
            if met in chamadas_classe_1 and met in chamadas_classe_2:
                a += 1
            elif met in chamadas_classe_1:
                b += 1
            elif met in chamadas_classe_2:
                c += 1
            else:
                d += 1
        return a, b, c, d
