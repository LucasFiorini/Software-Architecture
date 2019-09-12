import ast

def imprimeRelatorio(dup_list):
    while dup_list:
        first = dup_list.pop()
        print("Metodo " + first.nome + " repetido nas classes: ")
        print("\t"  + first.classe)

        for noh in dup_list:
            if noh.nome == first.nome:
                print("\t" + noh.classe)
                dup_list.remove(noh)

def separaDuplicatas(metodos_classes, dup_list):
    while metodos_classes:
        c = metodos_classes.pop()
        seen = False
        for met in metodos_classes:
            if met.nome == c.nome:
                dup_list.append(met)
                metodos_classes.remove(met)
                seen = True
        if seen:
            dup_list.append(c)

def percorreArvore(arvore, metodos_classes):
    for noh in ast.walk(arvore):
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
                            metodos_classes.append(c)
                    else:
                        c = InfoMetodo(classe.name, nome_metodo)
                        metodos_classes.append(c)


class InfoMetodo():
    nome = " "
    classe = " "

    def __init__(self, nomeClasse, nomeMetodo):
        self.nome = nomeMetodo
        self.classe = nomeClasse


with open("Exemplo.py", "r") as codigo_analisado:
    arvore = ast.parse(codigo_analisado.read())

metodos_classes = []


percorreArvore(arvore, metodos_classes)
dup_list = []

separaDuplicatas(metodos_classes, dup_list)

imprimeRelatorio(dup_list)
