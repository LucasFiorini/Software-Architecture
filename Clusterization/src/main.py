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
    classe_nova = input("Digite o nome da classe nova: ")
    map_classe_similaridade, lista_similaridades = calcular_similaridades(s, classe_nova)
    print()
    print("Similaridades entre as classes antigas:")
    imprimir_lista(list(map_classe_similaridade.values()))
    print()
    print("Similaridades entre a classe nova e as classes antigas:")
    print(lista_similaridades)
    print()
    lista_instancias = clusterizar(map_classe_similaridade, 0.3)
    print("Classes antigas clusterizadas:")
    imprimir_lista(lista_instancias)
    print()
    print("Veredito:")
    knn = KNN(2, lista_instancias, lista_similaridades)


if __name__ == '__main__':
    main()
