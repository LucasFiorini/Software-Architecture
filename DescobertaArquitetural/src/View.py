from graphviz import Digraph
from subprocess import check_call

cores = [
    "red2",
    "blue2",
    "green2",
    "gold2",
    "violetred",
    "grey20",
    "mediumpurple",
    "darkorange2",
    "crimson",
    "cyan2"
]

def constroi_grafo(map, lista_clusters):
    grafo = Digraph(comment='Arquitetura')
    for i in map.keys():
        grafo.node(i,i)
    for noh in map.keys():
        lista_arestas = map[noh]
        for vizinho in lista_arestas:
            grafo.edge(noh, vizinho)

    # Desenho dos clusters
    for id_cluster in range(len(lista_clusters)):
        cluster = Digraph("cluster_"+str(id_cluster))
        cluster.attr(color=cores[id_cluster])
        for nome_classe in lista_clusters[id_cluster]:
            cluster.node(nome_classe, nome_classe)
        grafo.subgraph(cluster)

    arquivo = open('Grafo.dot', 'w')
    arquivo.writelines(grafo.source)
    arquivo.close()

    check_call(['dot','-Tpng','Grafo.dot','-o','Grafo.png'])
