import ast
import astor

def template_controller():
    return ast.ClassDef(name='Controller', bases=[], keywords=[],\
            body=[], decorator_list=[])

def template_instanciacao(nome_model):
    nome_model = str(nome_model)
    return ast.Assign(targets=[ast.Name(id='objeto', ctx=ast.Store())], value=ast.Call(func=ast.Name(id=nome_model, ctx=ast.Load()), args=[], keywords=[]))

def template_met_controller(pos, nome_model):
    novo_nome_mt = "procedimento_" + str(pos)
    return ast.FunctionDef(name=novo_nome_mt, args=ast.arguments(args=[ast.arg(arg='view', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),\
        body=[template_instanciacao(nome_model)], decorator_list=[], returns=None)

def template_chamada(procedimento_chamado):
    return ast.Expr(value=ast.Call(func=ast.Attribute(value=ast.Name(id='Controller', ctx=ast.Load()), attr=procedimento_chamado, ctx=ast.Load()), args=[ast.arg(arg='self', annotation=None)], keywords=[]))

def template_met_view(nome_metodo, id_procedimento):
    novo_nome_mt = nome_metodo + "_novo"
    procedimento_chamado = "procedimento_" + str(id_procedimento)
    return ast.FunctionDef(name=novo_nome_mt, args=ast.arguments(args=[ast.arg(arg='self', annotation=None)], vararg=None, kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),\
        body=[template_chamada(procedimento_chamado)], decorator_list=[], returns=None)

class Analisador(ast.NodeVisitor):
    chamadas = []
    tem_input = False
    tem_print = False

    def visit_Call(self, chamada):
        # Reconhece inputs, prints e instanciacoes de objetos
        if isinstance(chamada.func, ast.Name):
            if chamada.func.id == "input":
                self.tem_input = True
            elif chamada.func.id == "print":
                self.tem_print = True
            else:
                self.chamadas.append(chamada.func.id)
        self.generic_visit(chamada)

    def limpar_atributos(self):
        self.chamadas = []
        self.tem_input = False
        self.tem_print = False


class GeradorDeFachada:
    nomes_views = []
    nomes_models = []

    # Leva o nome da classe aos nomes dos metodos problematicos
    map_classe_metodos = {}
    # Leva o nome do metodo aos nomes dos models instanciados
    map_metodo_models = {}

    qnt_classes = 0
    controller = None

    def __init__(self, caminho_arquivo):
        self.analisador = Analisador()
        with open(caminho_arquivo, "r") as codigo_analisado:
            self.arvore = ast.parse(codigo_analisado.read())
#            print(ast.dump(self.arvore))
        self.explorar_arvore()
        self.resolver_problemas()
        self.escrever_arquivo_solucao()

    def explorar_arvore(self):
        for classe in self.arvore.body:
            if isinstance(classe, ast.ClassDef):
                self.qnt_classes += 1
                if classe.name == "Controller":
                    self.controller = classe
                self.classificar(classe)
        for classe in self.arvore.body:
            if isinstance(classe, ast.ClassDef):
                for metodo in classe.body:
                    if isinstance(metodo, ast.FunctionDef):
                        if metodo.name != "__init__":
                            self.encontrar_vioalacoes(classe, metodo)

    def classificar(self, classe):
        self.analisador.limpar_atributos()
        self.analisador.visit(classe)
        if self.analisador.tem_input or self.analisador.tem_print:
            self.nomes_views.append(classe.name)
        else:
            self.nomes_models.append(classe.name)

    def encontrar_vioalacoes(self, classe, metodo):
        self.analisador.limpar_atributos()
        self.analisador.visit(metodo)
        lista_chamadas = self.analisador.chamadas
        models_instanciados = []
        for chamada in lista_chamadas:
            if chamada in self.nomes_models:
                models_instanciados.append(chamada)
        if models_instanciados:
            self.mapear_violacoes(classe, metodo, models_instanciados)

    def mapear_violacoes(self, classe, metodo, models_instanciados):
        self.map_metodo_models[metodo.name] = models_instanciados
        if classe.name in self.map_classe_metodos:
            self.map_classe_metodos[classe.name].append(metodo.name)
        else:
            self.map_classe_metodos[classe.name] = [metodo.name]

    def resolver_problemas(self):
        self.inicializar_controller()
        for classe in self.arvore.body:
            if isinstance(classe, ast.ClassDef):
                if classe.name in self.map_classe_metodos.keys():
                    nome_cl = classe.name
                    for metodo in classe.body:
                        if isinstance(metodo, ast.FunctionDef):
                            if metodo.name in self.map_classe_metodos[nome_cl]:
                                nome_mt = metodo.name
                                for nome_md in self.map_metodo_models[nome_mt]:
                                    self.adicionar_codigo_controller(nome_md)
                                    self.adicionar_codigo_view(classe, metodo)

    def inicializar_controller(self):
        if not self.controller:
            pos = self.qnt_classes
            self.arvore.body.insert(pos, template_controller())
            self.controller = self.arvore.body[pos]

    def adicionar_codigo_controller(self, nome_model):
        pos = len(self.controller.body)
        novo_mt = template_met_controller(pos, nome_model)
        self.controller.body.insert(pos, novo_mt)

    def adicionar_codigo_view(self, classe, metodo):
        pos = classe.body.index(metodo)
        pos += 1
        id_procedimento = len(self.controller.body) - 1
        novo_mt = template_met_view(metodo.name, id_procedimento)
        classe.body.insert(pos, novo_mt)

    def escrever_arquivo_solucao(self):
        novo_codigo = astor.to_source(self.arvore)
        arquivo = open("Novo.py", "w")
        arquivo.writelines(novo_codigo)


g = GeradorDeFachada("ExemploArq.py")
for met in g.map_metodo_models:
    print("No metodo \""+met+"\", nao deveriam ser instanciados os models:")
    print("   ", g.map_metodo_models[met])
    print()




#
