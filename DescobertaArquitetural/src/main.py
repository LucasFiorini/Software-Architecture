#TODO
# analisar de todas para todas classes o indice de Jacard e guardar em um map - OK
# fazer reconhecer chamadas de metodos feitas por instancias e nao apensa chamadas estaticas - doing

from Similaridade import Similaridade
from CalculoSimilaridades import calcular_similaridades
from Clusterizacao import clusterizar
import sys
from View import constroi_grafo

def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

def gerar_lista_clusters(lista_instancias):
    map_tipo_p_lista_nomes = {}
    for instancia in lista_instancias:
        tipo = instancia["Tipo"]
        if tipo not in map_tipo_p_lista_nomes.keys():
            map_tipo_p_lista_nomes[tipo] = [instancia["Nome"]]
        else:
            map_tipo_p_lista_nomes[tipo].append(instancia["Nome"])
    lista_clusters = []
    for cluster in map_tipo_p_lista_nomes.values():
        lista_clusters.append(cluster)
    return lista_clusters

def main():
    s = Similaridade("exemplo.py")
    map_classe_similaridade = calcular_similaridades(s)
    lista_instancias = clusterizar(map_classe_similaridade, float(sys.argv[1]))
    lista_clusters = gerar_lista_clusters(lista_instancias)
    constroi_grafo(s.map_classe_classe, lista_clusters)


if __name__ == '__main__':
    main()
