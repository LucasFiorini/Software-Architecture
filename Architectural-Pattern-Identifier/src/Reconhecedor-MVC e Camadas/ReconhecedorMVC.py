from Reconhecedor import Reconhecedor

class ReconhecedorMVC(Reconhecedor):
    models = []
    controllers = []

    def imprimir_relatorio(self, controller, views, models):
        print("M -", models)
        print("V -", views)
        print("C -", controller)

    def reconhecer_models(self):
        for classe in self.map_relacionamentos.keys():
            if not self.map_relacionamentos[classe]:
                if classe not in self.views:
                    self.models.append(classe)

    def reconhecer_controllers(self):
        for classe in self.map_relacionamentos.keys():
            # Flags
            interage_com_view = False
            interage_com_model = False
            for relacionada in self.map_relacionamentos[classe]:
                # Obs: as views sao reconhecidas na classe mae (Reconhecedor)
                if relacionada in self.views:
                    interage_com_view = True
                elif relacionada in self.models:
                    interage_com_model = True
            if interage_com_view and interage_com_model:
                self.controllers.append(classe)

    def reconhecer_mvc(self):
        self.reconhecer_models()
        self.reconhecer_controllers()
        if self.controllers:
            for controller in self.controllers:
                views = []
                models = []
                for classe in self.map_relacionamentos[controller]:
                    if classe in self.views:
                        views.append(classe)
                    elif classe in self.models:
                        models.append(classe)
                self.imprimir_relatorio(controller, views, models)


rec = ReconhecedorMVC("exemplos/" + "ExemploMVC2.py")
rec.reconhecer_mvc()
