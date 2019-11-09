import csv
import math

class KNN:

    def __init__(self, k, lista_instancias, lista_similaridades):
        self.k = k
        self.lista_instancias = self.copiar_lista_instancias(lista_instancias)
        self.lista_similaridades = lista_similaridades.copy()
        self.classificar()

    def copiar_lista_instancias(self, lista):
        nova_lista = []
        for instancia in lista:
            nova_instancia = {}
            nova_instancia["Nome"] = instancia["Nome"]
            nova_instancia["Tipo"] = instancia["Tipo"]
            nova_lista.append(nova_instancia)
        return nova_lista

    def classificar(self):
        tipos = []
        quantidades = []
        for i in range(self.k):
            vizinho = self.instancia_mais_similar()
            if vizinho["Tipo"] in tipos:
                pos = tipos.index(vizinho["Tipo"])
                quantidades[pos] += 1
            else:
                tipos.append(vizinho["Tipo"])
                quantidades.append(1)
        pos_maior = quantidades.index(max(quantidades))
        tipo_resultado = tipos[pos_maior]
        print("(k = "+str(self.k)+") -> A nova classe se encaixa melhor no tipo "+\
                str(tipo_resultado)+".")

    def instancia_mais_similar(self):
        pos = self.pos_maior_similaridade()
        instancia = self.lista_instancias.pop(pos)
        return instancia

    def pos_maior_similaridade(self):
        maior = -math.inf
        pos_maior = -1
        for similaridade in self.lista_similaridades:
            if similaridade > maior:
                pos_maior = self.lista_similaridades.index(similaridade)
                maior = similaridade
        self.lista_similaridades.pop(pos_maior)
        return pos_maior

#-------------------------------------------------------------------------------

lista_instancias_base = [\
    {"Nome":"Classe1", "Tipo":"A"},\
    {"Nome":"Classe2", "Tipo":"A"},\
    {"Nome":"Classe3", "Tipo":"B"},\
    {"Nome":"Classe4", "Tipo":"B"},\
    {"Nome":"Classe5", "Tipo":"A"},\
]

lista_coeficientes = [0.5, 0.1, 0.7, 1.0, 0.2]

knn = KNN(3, lista_instancias_base, lista_coeficientes)
print()
knn = KNN(5, lista_instancias_base, lista_coeficientes)
print()
