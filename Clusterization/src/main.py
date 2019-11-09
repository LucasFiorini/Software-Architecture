#TODO
# analisar de todas para todas classes o indice de Jacard e guardar em um map - OK
# fazer reconhecer chamadas de metodos feitas por instancias e nao apensa chamadas estaticas - doing

from Similaridade import Similaridade
from CalculoSimilaridades import calcular_similaridades
from Clusterizacao import clusterizar
from KNN import KNN

def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

def main():
    s = Similaridade("exemplo.py")
    map_classe_similaridade = calcular_similaridades(s)

    classe_nova = input("Digite o nome da classe nova: ")
    if classe_nova not in map_classe_similaridade.keys():
        lista_similaridades = []
        print("Classe nao encontrada!\n")
    else:
        print()
        lista_similaridades = map_classe_similaridade[classe_nova]
        imprimir_lista(list(map_classe_similaridade.values()))
        print()
        lista_instancias = clusterizar(map_classe_similaridade, 0.3)
        imprimir_lista(lista_instancias)
        print()

        knn = KNN(3, lista_instancias, lista_similaridades)


if __name__ == '__main__':
    main()
