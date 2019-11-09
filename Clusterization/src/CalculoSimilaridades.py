# Metodo que retorna um map onde as chaves sao
# os nomes de todas as classes e cada indice guarda uma lista
# que contem a indice de similaridade de Jacard entre a chave e
# todas as outras classes

from Coefficients import Statistics

def calcular_similaridades(s):
    map_classe_similaridade = {}
    for classe1 in s.map_classe_metodos.keys():
        lista_indices_jaccard = []
        for classe2 in s.map_classe_metodos.keys():
            try:
                # print("classe 1: " + classe1 + "Classe 2: " + classe2)
                a, b, c, d = s.calcular_coeficientes(str(classe1), str(classe2))
                # print("{} {} {} {}".format(a,b,c,d))
                lista_indices_jaccard.append(Statistics.Jaccard(a, b, c))
                # print(lista_indices_jaccard)
            except:
                continue
            map_classe_similaridade[classe1] = lista_indices_jaccard
    return map_classe_similaridade
