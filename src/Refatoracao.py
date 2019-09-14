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

    def imprimir_mapeamento(self):
        for metodo in self.map_metodos:
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
                superclasse = self.encontrar_classe_pelo_nome(nome_superclasse)
                for metodo in classe.body:
                    if isinstance(metodo, ast.FunctionDef):
                        nome_metodo = metodo.name
                        if nome_metodo != "__init__":
                            # Classes que nao herdam sao ignoradas
                            if nome_superclasse != "":
                                info = InfoClasse(classe, superclasse)
                                if nome_metodo not in self.map_metodos:
                                    self.map_metodos[nome_metodo] = [info]
                                else:
                                    self.map_metodos[nome_metodo].append(info)

    def iniciar_dialogo_para_refatoracao(self):
        print("Deseja refatorar? (s/n)")
        op = input()
        if op == "s":
            nome_metodo =\
                input("Digite o nome do metodo que deseja subir para a superclasse: ")
            nome_superclasse = input("Digite o nome da superclasse destino: ")
            return nome_metodo, nome_superclasse
        else:
            return "", ""


class Refatorador():
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


arquivo = "Exemplo.py"
with open(arquivo, "r") as codigo_analisado:
    arvore = ast.parse(codigo_analisado.read())

a = AnalisadorDeArvore(arvore)
a.imprimir_mapeamento()
nome_metodo, nome_superclasse = a.iniciar_dialogo_para_refatoracao()

if nome_metodo != "" and nome_superclasse != "":
    ref = Refatorador()
    metodo_foi_adicionado_na_superclasse = False

    # Tratamento para caso o usuario digite algum nome errado
    try:
        for metodo in a.map_metodos:
            if metodo == nome_metodo:
                for info_classe in a.map_metodos[metodo]:
                    superclasse = info_classe.noh_superclasse.name
                    if superclasse == nome_superclasse:
                        ref.remover_metodo(nome_metodo, info_classe.noh_proprio)
                        if not metodo_foi_adicionado_na_superclasse:
                            ref.injetar_metodo(nome_metodo, info_classe.noh_superclasse)
                            metodo_foi_adicionado_na_superclasse = True
        ref.escrever_novo_codigo_no_arquivo(arvore, arquivo)
    except:
        print("Algum nome foi digitado errado!")
