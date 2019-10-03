from Reconhecedor import Reconhecedor

class ReconhecedorCamadas(Reconhecedor):
    def imprimir_relatorio(self, camadas):
        if camadas != None:
            for indice in camadas.keys():
                print("Camada", indice, "->", camadas[indice])
        else:
            print("O sistema nao estah arquitetado em camadas!")

    def reconhecer_camadas(self):
        camadas = {}
        atual = 1
        abaixo = 2
        camadas[atual] = self.views
        classes_aparecidas = []
        while camadas[atual]:
            camadas[abaixo] = []
            for classe in camadas[atual]:
                for relacionada in self.map_relacionamentos[classe]:
                    if relacionada in classes_aparecidas:
                        return None
                    elif relacionada in camadas[atual] or\
                            relacionada in camadas[abaixo]:
                        pass
                    else:
                        camadas[abaixo].append(relacionada)
            classes_aparecidas += camadas[atual]
            atual = abaixo
            abaixo += 1
        self.imprimir_relatorio(camadas)


rec = ReconhecedorCamadas("exemplos/" + "ExCamadas.py")
#print(rec.map_metodo_classe)
#print(rec.map_classe_chamadas)
#print(rec.map_relacionamentos)
#print(rec.views)
#print()
rec.reconhecer_camadas()
