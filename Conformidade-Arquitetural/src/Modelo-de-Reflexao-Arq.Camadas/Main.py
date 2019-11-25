from ReconhecedorCamadas import ReconhecedorCamadas
from GeradorGrafo import constroi_grafo

rec = ReconhecedorCamadas("Exemplos/ExCamadas.py")
rec.reconhecer_camadas()

lista_clusters = []
for cluster in rec.camadas.values():
    lista_clusters.append(cluster)

# Verifica ausencias
ausencias = []
for classe in rec.map_relacionamentos.keys():
    clusterizada = False
    for cluster in lista_clusters:
        if classe in cluster:
            clusterizada = True
    if not clusterizada:
        ausencias.append(classe)

print(rec.map_relacionamentos)
print(lista_clusters)
print(ausencias)

constroi_grafo(rec.map_relacionamentos, lista_clusters, rec.violacoes, ausencias)
