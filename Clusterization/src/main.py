#TODO
# analisar de todas para todas classes o indice de Jacard e guardar em um map - OK
# fazer reconhecer chamadas de metodos feitas por instancias e nao apensa chamadas estaticas - doing
from Similaridade import Similaridade
from CalculoSimilaridades import calcular_similaridades
from Clusterizacao import clusterizar

def main():
    s = Similaridade("exemplo.py")
    map_classe_similaridade = calcular_similaridades(s)
    for lista in map_classe_similaridade.values():
        print(lista)
    print()
    clusterizar(map_classe_similaridade, 0.3)


if __name__ == '__main__':
    main()
