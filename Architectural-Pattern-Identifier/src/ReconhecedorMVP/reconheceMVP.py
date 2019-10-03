import ast

class ReconheceMVP:
    lista_classes = []
    map_metodos_classes = {}
    map_chamadas_classes = {}

    def __init__(self, arquivo):
        with open(arquivo, "r") as codigo_analisado:
            arvore = ast.parse(codigo_analisado.read())
            #print(ast.dump(arvore))
            for classe in ast.walk(arvore):
                if isinstance(classe, ast.ClassDef):
                    self.lista_classes.append(classe)

    def reconhecer_mvp(self):
        for classe in self.lista_classes:
            self.preenche_map(classe)
        for classe in self.lista_classes:
            self.identifica_chamadas(classe)
        if not self.encontra_view():
            print("View nao encontrada! Abortando busca\n")

    def encontra_presenter(self, nome_view):
        for elemento in self.map_chamadas_classes[nome_view]:
            if nome_view not in self.map_chamadas_classes[elemento]:
                for model in self.map_chamadas_classes[elemento]:
                    if len(self.map_chamadas_classes[model]) == 0:
                        print("Classe Model implementada pela classe: " + model)
                        print("Classe Presenter implementada pela classe: " + elemento)
                        return True
        return False

    def encontra_view(self):
        view_encontrada = False

        for classe in self.map_metodos_classes.keys():
            eh_view = True
            for chamadas in self.map_chamadas_classes.keys():
                if len(self.map_chamadas_classes[chamadas]) > 1:
                    if classe in self.map_chamadas_classes[chamadas]:
                        eh_view = False
            if eh_view:
                if self.checar_interface_usuario(classe):
                    if self.encontra_presenter(classe):
                        view_encontrada = True
                        print("Classe View implementada pela classe:" + classe)
                        print("########################################################")


        return view_encontrada


    def checar_interface_usuario(self, classe_view):
        for classe in self.lista_classes:
            if classe_view == classe.name:
                for elemento in classe.body:
                    if isinstance(elemento, ast.FunctionDef):
                        for info in elemento.body:
                            try:
                                if info.value.func.id == "input":
                                    return True
                            except:
                                continue
        return False

    def identifica_chamadas(self, classe):
        nome_classe = classe.name
        for metodo in classe.body:
            if isinstance(metodo, ast.FunctionDef):
                for chamadas in metodo.body:
                    try:
                        nome_prefixo = self.reconhece_prefixo(chamadas)
                        nome_metodo = chamadas.value.func.attr
                        local, nome_c = self.verifica_nacionalidade(nome_metodo, nome_classe, nome_prefixo)
                        if not local:
                            if nome_classe not in self.map_chamadas_classes:
                                self.map_chamadas_classes[nome_classe] = [nome_c]
                            else :
                                self.map_chamadas_classes[nome_classe].append(nome_c)
                    except:
                        continue
        if nome_classe not in self.map_chamadas_classes:
            self.map_chamadas_classes[nome_classe] = ""

    def verifica_nacionalidade(self, nome_metodo, nome_classe, nome_prefixo):
        if nome_metodo in self.map_metodos_classes[nome_classe]:
            return True, " "
        else:
            name = " "
            for classe in self.map_metodos_classes.keys():
                if classe == nome_prefixo:
                    if nome_metodo in self.map_metodos_classes[classe] and classe != nome_classe:
                        name = classe
            return False, name


    def preenche_map(self,classe):
        nome_classe = classe.name
        for metodo in classe.body:
            if isinstance(metodo, ast.FunctionDef):
                if nome_classe not in self.map_metodos_classes:
                    self.map_metodos_classes[nome_classe] = [metodo.name]
                else:
                    self.map_metodos_classes[nome_classe].append(metodo.name)


    def reconhece_prefixo(self, chamada):
        try:
            nome_prefixo = chamada.value.func.value.id;
            return nome_prefixo
        except:
            pass

r = ReconheceMVP("exemplos/" + "exemploRuim.py")
r.reconhecer_mvp()
#print(r.map_chamadas_classes)
#print(r.map_metodos_classes)