import ast


class InfoMetodo:
    vezes_chamado = 0
    nome_metodo = ''

    def __init__(self, nome_metodo):
        self.nome_metodo = nome_metodo
        self.vezes_chamado = 1


class InfoClass:
    name = ''
    qtd_conditional = 0
    qtd_loop = 0
    qtd_print = 0
    qtd_input = 0
    qtd_open = 0
    qtd_try = 0
    metodos_externos = []

    def __init__(self, name, lista_atributos, lista_metodos):
        self.name = name
        self.qtd_conditional = lista_atributos[0]
        self.qtd_loop = lista_atributos[0]
        self.qtd_print = lista_atributos[1]
        self.qtd_input = lista_atributos[2]
        self.qtd_open = lista_atributos[3]
        self.qtd_try = lista_atributos[4]
        self.metodos_externos = lista_metodos


class Similaridade:

    arvore = None
    map_classe_metodos = {}
    analisador = None
    lista_info_classes = []

    def __init__(self, caminho_arquivo):
        with open(caminho_arquivo, "r") as codigo_analisado:
            self.arvore = ast.parse(codigo_analisado.read())
#            print(ast.dump(self.arvore))
            self.analisador = Analisador()
        self.explorar_arvore()
        self.filtrar_metodos()

    def filtrar_metodos(self):
        for classe in self.lista_info_classes:
            lista_filtrada = []
            for metodo in classe.metodos_externos:
                if self.eh_externo(metodo, classe.name):
                    if not self.find(metodo, lista_filtrada):
                        novo_metodo = InfoMetodo(metodo)
                        lista_filtrada.append(novo_metodo)
                    else:
                        lista_filtrada[self.encontra_indice(metodo, lista_filtrada)].vezes_chamado += 1
            classe.metodos_externos = lista_filtrada

    @staticmethod
    def encontra_indice(metodo_procurado, lista):
        i = 0
        for metodo in lista:
            if metodo_procurado == metodo.nome_metodo:
                return i
            i += 1

    @staticmethod
    def find(nome_metodo, lista):
        for elemntos in lista:
            if elemntos.nome_metodo == nome_metodo:
                return True
        return False

    def eh_externo(self, nome_metodo, nome_classe):
        if nome_metodo not in self.map_classe_metodos[nome_classe]:
            return True
        return False

    def explorar_arvore(self):
        lista_aux = []
        for classe in self.arvore.body:
            if isinstance(classe, ast.ClassDef):
                self.analisador.visit(classe)
                self.map_classe_metodos[classe.name] = self.analisador.get_list_metodos()
                lista_aux.append(self.analisador.qtd_conditional)
                lista_aux.append(self.analisador.qtd_loop)
                lista_aux.append(self.analisador.qtd_print)
                lista_aux.append(self.analisador.qtd_input)
                lista_aux.append(self.analisador.qtd_open)
                lista_aux.append(self.analisador.qtd_try)
                i = InfoClass(classe.name, lista_aux, self.analisador.lista_chamadas)
                self.lista_info_classes.append(i)
                self.analisador.clear_list()


class Analisador(ast.NodeVisitor):
    lista_metodos = []
    lista_chamadas = []
    qtd_conditional = 0
    qtd_loop = 0
    qtd_print = 0
    qtd_input = 0
    qtd_open = 0
    qtd_try = 0

    def visit_If(self, classe):
        self.qtd_conditional += 1

    def visit_For(self, classe):
        self.qtd_loop += 1

    def visit_Try(self, classe):
        self.qtd_try += 1

    def visit_While(self, classe):
        self.qtd_loop += 1

    def visit_FunctionDef(self, classe):
        self.lista_metodos.append(classe.name)
        self.generic_visit(classe)

    def visit_Call(self, classe):
        if isinstance(classe.func, ast.Attribute):
            self.lista_chamadas.append(classe.func.attr)

        if isinstance(classe.func, ast.Name):
            if classe.func.id == "input":
                self.qtd_input += 1
            elif classe.func.id == "print":
                self.qtd_print += 1
            elif classe.func.id == "open":
                self.qtd_open += 1
        self.generic_visit(classe)

    def get_list_metodos(self):
        return self.lista_metodos

    def clear_list(self):
        self.lista_metodos = []
        self.qtd_conditional = 0
        self.qtd_loop = 0
        self.qtd_input = 0
        self.qtd_print = 0
        self.qtd_open = 0
        self.qtd_try = 0
        self.lista_chamadas = []


def main():
    g = Similaridade("exemplo.py")
    print(g.lista_info_classes[0].metodos_externos[0].nome_metodo)
    print(g.lista_info_classes[0].metodos_externos[0].vezes_chamado)


if __name__ == '__main__':
    main()

#TODO
# arrumar contagem de prints que estao dentro de if/else pois ele os desconsidera
# inventar alguma metrica para as informações coletadas
# tentar separar as classes em MVP
# interface de escolha para o usuário entre comprar uma classe com todas, duas especificas ou todas com todas
# colocar comentarios