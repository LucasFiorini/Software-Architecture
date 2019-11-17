#TODO
# analisar de todas para todas classes o indice de Jacard e guardar em um map - OK
# fazer reconhecer chamadas de metodos feitas por instancias e nao apensa chamadas estaticas - doing

from Similaridade import Similaridade
from CalculoSimilaridades import calcular_similaridades
from Clusterizacao import clusterizar
from KNN import KNN
import sys
from View import Grafo

def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

def main():
    s = Similaridade(sys.argv[1])
    classe_nova = sys.argv[2]
    map_classe_similaridade, lista_similaridades = calcular_similaridades(s, classe_nova)
    if not lista_similaridades:
        print("Classe nao existente!")
    else:
        #print("Similaridades entre as classes antigas:")
        imprimir_lista(list(map_classe_similaridade.values()))
        #print()
        #print("Similaridades entre a classe nova e as classes antigas:")
        #print(lista_similaridades)
        #print()
        lista_instancias = clusterizar(map_classe_similaridade, float(sys.argv[3]))
        #print("Classes antigas clusterizadas:")
        #imprimir_lista(lista_instancias)
        #print()
        #print("Veredito:")
        knn = KNN(int(sys.argv[4]), lista_instancias, lista_similaridades)
        Grafo.constroi_grafo(s.map_classe_classe)


if __name__ == '__main__':
    main()
