import ast

class ReconhecedorDecorator:
    lista_classes = []

    def __init__(self, arquivo):
        with open(arquivo, "r") as codigo_analisado:
            arvore = ast.parse(codigo_analisado.read())
#            print(ast.dump(arvore))
            for classe in ast.walk(arvore):
                if isinstance(classe, ast.ClassDef):
                    self.lista_classes.append(classe)

    def eh_abstrata(self, classe):
        if classe.decorator_list:
            return True
        else:
            return False

    # Retorna duas listas de classes filhas da classe cujo nome foi passado,
    # uma contendo as classes concretas e outra contendo as classes abstratas
    def obter_filhas(self, nome_classe):
        filhas_concretas = []
        filhas_abstratas = []
        for classe in self.lista_classes:
            if classe.bases:
                if classe.bases[0].id == nome_classe:
                    if self.eh_abstrata(classe):
                        filhas_abstratas.append(classe)
                    else:
                        filhas_concretas.append(classe)
        return filhas_concretas, filhas_abstratas

    # Retorna True se a classe possui um atributo privado chamado
    # instancia decoradora
    def possui_atributo_instancia(self, classe):
        for atribuicao in classe.body:
            if isinstance(atribuicao, ast.Assign):
                if atribuicao.targets[0].id == "instancia_decorada":
                    return True
        return False

    def reconhecer_decorator(self):
        for classe in self.lista_classes:
            nome_classe = classe.name
            if self.eh_abstrata(classe):
                filhas_concretas, filhas_abstratas = self.obter_filhas(nome_classe)
                if len(filhas_abstratas) == 1:
                    classe_decoradora = filhas_abstratas[0]
                    nome_decoradora = classe_decoradora.name
                    if self.possui_atributo_instancia(classe_decoradora):
                        print("Decorator identificado!")
                        print()
                        print("Interface:")
                        print("--------------------", nome_classe)
                        print()
                        print("Classes concretas:")
                        for classe in filhas_concretas:
                            print("--------------------", classe.name)
                        print()
                        print("Classe decoradora:")
                        print("--------------------", nome_decoradora)
                        print()
                        print("Decoracoes:")
                        decoracoes, outras = self.obter_filhas(nome_decoradora)
                        for dec in decoracoes:
                            print("--------------------", dec.name)
