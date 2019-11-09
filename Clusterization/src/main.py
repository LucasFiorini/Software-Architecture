#TODO
# analisar de todas para todas classes o indice de Jacard e guardar em um map - OK
# fazer reconhecer chamadas de metodos feitas por instancias e nao apensa chamadas estaticas - doing
from Similaridade import Similaridade
from Knn import Knn


def main():
    s = Similaridade("exemplo.py")
    k = Knn(s)
    print(k.map_classe_similaridade, sep="\n")


if __name__ == '__main__':
    main()
