from Reconhecedor import Reconhecedor

class ReconhecedorCamadas(Reconhecedor):

    def reconhecer_camadas(self):
        camadas = {}
        classes_aparecidas = []
        lista_violacoes = [] # Lista de tuplas
        acima = 0
        corrente = 1
        abaixo = 2
        camadas[acima] = []
        camadas[corrente] = self.views
        while camadas[corrente]:
            camadas[abaixo] = []
            for classe in camadas[corrente]:
                for relacionada in self.map_relacionamentos[classe]:
                    if relacionada in classes_aparecidas:
                        lista_violacoes.append((classe, relacionada))
                    elif relacionada in camadas[acima] or\
                            relacionada in camadas[corrente] or\
                            relacionada in camadas[abaixo]:
                        pass
                    else:
                        camadas[abaixo].append(relacionada)
            classes_aparecidas += camadas[acima]
            acima = corrente
            corrente = abaixo
            abaixo += 1
        self.camadas = camadas
        self.violacoes = lista_violacoes
