# Retorna uma letra de acordo com o numero
def letra_correspondente(numero):
    letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return letras[numero]

# Agrupa as classes do meapeamento de acordo com a similaridade entre elas
def clusterizar(map_classe_similaridade, similaridade_limitante):
    map_classe_seu_grupo = {}

    # Cada grupo contem uma instancia, inicialmente
    for nome in map_classe_similaridade.keys():
        instancia = {"Nome":nome, "Tipo":None}
        novo_grupo = [instancia]
        map_classe_seu_grupo[nome] = novo_grupo

    # Analise dos coeficientes para o merge dos grupos
    for nome in map_classe_similaridade.keys():
        for ind_coeficiente in range(len(map_classe_similaridade[nome])):
            coeficiente = map_classe_similaridade[nome][ind_coeficiente]
            if coeficiente >= similaridade_limitante:
                classe1 = nome
                classe2 = list(map_classe_similaridade.keys())[ind_coeficiente]
                # Impede comparacao entre uma classe e ela mesma
                if classe1 != classe2:
                    grupo1 = map_classe_seu_grupo[classe1]
                    grupo2 = map_classe_seu_grupo[classe2]
                    # Construir grupo novo
                    for elemento in grupo2:
                        if elemento not in grupo1:
                            # Merge dos grupos
                            grupo1.append(elemento)
                            # Atualizacao da referencia para o grupo
                            map_classe_seu_grupo[elemento["Nome"]] = grupo1

    # Discernimento de cada grupo
    lista_grupos = []
    for grupo in map_classe_seu_grupo.values():
        if grupo not in lista_grupos:
            lista_grupos.append(grupo)

    # Discernimento de cada instancia
    lista_instancias = []
    for ind_grupo in range(len(lista_grupos)):
        grupo = lista_grupos[ind_grupo]
        for instancia in grupo:
            instancia["Tipo"] = letra_correspondente(ind_grupo)
            lista_instancias.append(instancia)

    return lista_instancias
