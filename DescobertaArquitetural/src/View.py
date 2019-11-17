from graphviz import Digraph
class Grafo:
    @staticmethod
    def constroi_grafo(map):
        grafo = Digraph(comment='Arquitetura')
        for i in map.keys():
            grafo.node(i,i)
        for noh in map.keys():
            lista_arestas = map[noh]
            for vizinho in lista_arestas:
                grafo.edge(noh, vizinho)
        print(grafo.source)

    # @staticmethod
    # def gera_arestas(map):
    #     lista_arestas = []
    #     for classe in map.keys():
    #         lista_classes = map[classe]
    #         for i in lista_classes:
    #             lista_arestas.append(classe + i)
    #     return lista_arestas