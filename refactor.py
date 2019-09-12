import ast


def imprime_relatorio(lista_duplicatas):
    while dup_list:
        first = lista_duplicatas.pop()
        print("Metodo " + first.nome + " repetido nas classes: ")
        print("\t" + first.classe)

        for noh in dup_list:
            if noh.nome == first.nome:
                print("\t" + noh.classe)
                lista_duplicatas.remove(noh)


def separa_duplicatas(lista_metodos_classes, lista_duplicatas):
    while lista_metodos_classes:
        c = lista_metodos_classes.pop()
        seen = False
        for met in lista_metodos_classes:
            if met.nome == c.nome:
                lista_duplicatas.append(met)
                lista_metodos_classes.remove(met)
                seen = True
        if seen:
            lista_duplicatas.append(c)


def percorre_arvore(arvore_gerada, lista_metodos_classes):
    for noh in ast.walk(arvore_gerada):
        if not isinstance(noh, ast.ClassDef):
            continue
        classe = noh
        if isinstance(classe, ast.ClassDef):
            for metodos_classe in classe.body:
                if isinstance(metodos_classe, ast.FunctionDef):
                    nome_metodo = metodos_classe.name
                    if nome_metodo[0] == '_' and nome_metodo[1] == '_':
                        # Ignorando construtor
                        if nome_metodo != "__init__":
                            c = InfoMetodo(classe.name, nome_metodo)
                            lista_metodos_classes.append(c)
                    else:
                        c = InfoMetodo(classe.name, nome_metodo)
                        lista_metodos_classes.append(c)


class InfoMetodo():
    nome = " "
    classe = " "

    def __init__(self, nome_classe, nome_metodo):
        self.nome = nome_metodo
        self.classe = nome_classe


with open("Exemplo.py", "r") as codigo_analisado:
    arvore = ast.parse(codigo_analisado.read())

metodos_classes = []


percorre_arvore(arvore, metodos_classes)
dup_list = []

separa_duplicatas(metodos_classes, dup_list)

imprime_relatorio(dup_list)
