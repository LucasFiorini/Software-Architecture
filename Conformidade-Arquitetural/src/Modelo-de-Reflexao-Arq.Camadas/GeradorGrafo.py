from graphviz import Digraph
from subprocess import check_call

def constroi_grafo(map, lista_clusters, lista_violacoes, lista_ausencias):
    grafo = Digraph(comment='Arquitetura')
    for i in map.keys():
        if i not in lista_ausencias:
            grafo.node(i,i)
        else:
            grafo.node(i,i, color="goldenrod3")
    for noh in map.keys():
        lista_arestas = map[noh]
        for vizinho in lista_arestas:
            if (noh, vizinho) not in lista_violacoes:
                grafo.edge(noh, vizinho)
            else:
                grafo.edge(noh, vizinho, color="crimson")

    # Desenho dos clusters
    for id_cluster in range(len(lista_clusters)):
        cluster = Digraph("cluster_"+str(id_cluster))
        cluster.attr(color="grey20")
        cluster.attr(label=str(id_cluster))
        for nome_classe in lista_clusters[id_cluster]:
            cluster.node(nome_classe, nome_classe)
        grafo.subgraph(cluster)

    arquivo = open('Grafo.dot', 'w')
    arquivo.writelines(grafo.source)
    arquivo.close()

    check_call(['dot','-Tpng','Grafo.dot','-o','Grafo.png'])
