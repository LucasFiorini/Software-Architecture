import ast
import astor

class InfoClasse():
    def __init__(self, noh_proprio, noh_superclasse):
        self.noh_proprio = noh_proprio
        self.noh_superclasse = noh_superclasse


class AnalisadorDeArvore():
    map_metodos = {}

    def __init__(self, arvore):
        self.mapear_metodos(arvore)

    def mostrar_metodos_repetidos(self):
        for metodo in self.map_metodos:
            if len(a.map_metodos[metodo]) > 1:
                print("O metodo", metodo, "estah repetido nas classes:")
                for info in a.map_metodos[metodo]:
                    print("   ", info.noh_proprio.name,\
                    "( super ->", info.noh_superclasse.name, ")")
                print()

    def capturar_nome_superclasse(self, noh_classe):
        if not noh_classe.bases:
            return ""
        else:
            return noh_classe.bases[0].id

    def encontrar_classe_pelo_nome(self, nome):
        for classe in ast.walk(arvore):
            if isinstance(classe, ast.ClassDef):
                if classe.name == nome:
                    return classe

    # Mapea o nome de cada metodo a uma lista de objetos do tipo InfoClasse.
    # Cada objeto desse tipo armazena o noh da classe que possui o método em
    # questao, assim como o noh da superclasse desta.
    def mapear_metodos(self, arvore):
        for classe in ast.walk(arvore):
            if isinstance(classe, ast.ClassDef):
                nome_superclasse = self.capturar_nome_superclasse(classe)
                if nome_superclasse != "":
                    superclasse = self.encontrar_classe_pelo_nome(nome_superclasse)
                for metodo in classe.body:
                    if isinstance(metodo, ast.FunctionDef):
                        nome_metodo = metodo.name
                        if nome_metodo != "__init__":
                            # Classes que nao herdam sao ignoradas
                            if nome_superclasse != "":
                                info = InfoClasse(classe, superclasse)
                                if nome_metodo not in self.map_metodos:
                                else:
                                    self.map_metodos[nome_metodo].append(info)


class Refatorador():
    def __init__(self, analisador_arvore):
        self.analisador = analisador_arvore

    def injetar_metodo(self, nome_metodo, noh_classe):
        noh_definicao_funcao = ast.FunctionDef\
                (name=nome_metodo, args=ast.arguments(args=["self"], vararg=None,\
                kwonlyargs=[], kw_defaults=[], kwarg=None, defaults=[]),\
                body=[ast.Pass()], decorator_list=[], returns=None)
        noh_classe.body.append(noh_definicao_funcao)

    def remover_metodo(self, nome_metodo, noh_classe):
        for noh in noh_classe.body:
            if isinstance(noh, ast.FunctionDef):
                if noh.name == nome_metodo:
                    noh_classe.body.remove(noh)

    def escrever_novo_codigo_no_arquivo(self, arvore, caminho_arquivo):
        novo_codigo = astor.to_source(arvore)
        arquivo = open(caminho_arquivo, "w")
        arquivo.writelines(novo_codigo)

    def apresentar_refatoracoes_possiveis(self):
        nenhuma_refatoracao_possivel = True
        for metodo in self.analisador.map_metodos:
            if len(self.analisador.map_metodos[metodo]) > 1:
                nenhuma_refatoracao_possivel = False
                lista_infoclasses = self.analisador.map_metodos[metodo]
                superclasse = lista_infoclasses[0].noh_superclasse.name
                print("Deseja subir o metodo", metodo, \
                        "para a superclasse", superclasse, "? (s/n)")
                if input() == "s":
                    self.subir_metodo(metodo)
        if nenhuma_refatoracao_possivel:
            print("Nenhuma refatoracao possivel!")

    def subir_metodo(self, nome_metodo):
        metodo_foi_adicionado_na_superclasse = False
        for info_classe in self.analisador.map_metodos[nome_metodo]:
            superclasse = info_classe.noh_superclasse.name
            ref.remover_metodo(nome_metodo, info_classe.noh_proprio)
            if not metodo_foi_adicionado_na_superclasse:
                ref.injetar_metodo(nome_metodo, info_classe.noh_superclasse)
                metodo_foi_adicionado_na_superclasse = True


arquivo = "Exemplo.py"
with open(arquivo, "r") as codigo_analisado:
    arvore = ast.parse(codigo_analisado.read())

a = AnalisadorDeArvore(arvore)
a.mostrar_metodos_repetidos()

print("-----------------------------------------------------------------------")

ref = Refatorador(a)
ref.apresentar_refatoracoes_possiveis()

ref.escrever_novo_codigo_no_arquivo(arvore, arquivo)
