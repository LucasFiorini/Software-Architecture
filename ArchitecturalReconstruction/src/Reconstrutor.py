import ast
import sys
from Analisador import Analisador

class Reconstrutor:
    map_metodos = {}
    map_chamadas_metodos = {}
    analisador = None

    def __init__(self):
        arquivo = "Exemplo.py"
        with open(arquivo,"r") as codigo_analisado:
            arvore = ast.parse(codigo_analisado.read())
        self.analisador = Analisador()
        self.mapear_metodos(arvore)

    def mapear_metodos(self, arvore):
        encontrou_util = False
        for classe in arvore.body:
            if isinstance(classe, ast.ClassDef):
                if classe.name == 'Util':
                    encontrou_util = True
                self.analisador.limpar_atributos()
                self.analisador.visit(classe)
                self.map_chamadas_metodos[classe.name] = self.analisador.lista_chamadas
                self.map_metodos[classe.name] = self.analisador.lista_metodos
        if not encontrou_util:
            print("Classe Util nao encontrada para analise!")
            print("\nAbortando execucao")
            sys.exit()

    def encontrar_uso_util(self):
        map_move_method = {}
        for metodo in self.map_metodos['Util']:
            lista_utlizadores_util = []
            for chamadas in self.map_chamadas_metodos.keys():
                if metodo in self.map_chamadas_metodos[chamadas]:
                     lista_utlizadores_util.append(chamadas)
            if (len(lista_utlizadores_util) == 1):
                print("O Método " + metodo + " pode ser movido para a classe: " + lista_utlizadores_util[0])
                map_move_method[lista_utlizadores_util[0]] = metodo
        return map_move_method