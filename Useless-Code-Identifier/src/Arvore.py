'''
    A funcionalidade deste projeto eh fazer uma analise estatica em cima de
    um codigo da linguagem python para encontrar metodos que nao foram utlilizados
    em lugar nenhum do programa.

    Utilizando a AST gerada do programa passado para analise, todos os metodos encontrados
    sao colocados dentro de listas. Estas sao separadas pela visibilidade dos metodos(publico e privado).
    Logo, a arvore eh percorrida para encontrar as chamadas dos metodos. Os metodos que foram chamados em algum
    lugar do codigo sao removidos das listas, sobrando nelas apenas metodos nao chamados dentro do programa.
'''

import ast

with open("Exemplo.py", "r") as codigo_analisado:
    arvore = ast.parse(codigo_analisado.read())

#listas que guardam todos os metodos do programa
#uma classe por vez
metodos_privados = []
metodos_publicos = []


'''
Iterador para andar pelos nohs da arvore
:param variavel que guarda o codigo depois de fazer parse 
'''
for noh in ast.walk(arvore):
    if not isinstance(noh, ast.ClassDef):
        continue
    classe = noh
    #Verificacao  se o noh representa uma definicao de uma classe
    if isinstance(classe, ast.ClassDef):
        print("Classe --> " + str(classe.name))
        #Coloca todos os métodos da classe nas listas
        for metodos_classe in classe.body:
            if isinstance(metodos_classe, ast.FunctionDef):
                nome_metodo = metodos_classe.name
                if nome_metodo[0] == '_' and nome_metodo[1] == '_':
                    #Ignorando construtor
                    if nome_metodo != "__init__":
                        metodos_privados.append(nome_metodo)
                else:
                    metodos_publicos.append(nome_metodo)
        for elemento in classe.body:
            if isinstance(elemento, ast.FunctionDef):
                #A partir daqui sabe-se que o elemento eh um metodo
                metodo = elemento
                #Imprimi-se os nomes dos metodos desta classe
                for linha in metodo.body:
                    #Se o elemento em questao eh uma chamada de metodo
                    if isinstance(linha, ast.Expr) and isinstance(linha.value, ast.Call):
                        nome_chamada = linha.value.func.attr
                        if nome_chamada in metodos_privados:
                            metodos_privados.remove(nome_chamada)
                        elif nome_chamada in metodos_publicos:
                            metodos_publicos.remove(nome_chamada)
                        else:
                            pass
        #Varredura da arvore em que a raiz eh o noh main
        #para encontrar chamadas feitas nesse escopo do programa
        for node in ast.walk(arvore):
            if not isinstance(node, ast.ClassDef):
                if isinstance(node, ast.FunctionDef):
                    if node.name == "main":
                        for i in ast.walk(node):
                            '''
                                Nesse ponto o noh percorrido precisa 
                                    | nao ser uma definicao de classe
                                    | uma definicao de funcao
                                    | uma chamada de funcao
                                Isso significa que está dentro da subarvore do noh "main"
                                e eh uma chamada de funcao
                            '''
                            if isinstance(i, ast.Expr) and isinstance(i.value, ast.Call):
                                nome_metodo = i.value.func.attr
                                #remocao dos metodos chamados no escopo main do programa
                                if nome_metodo in metodos_privados:
                                    if nome_metodo != "__init__":
                                        metodos_privados.remove(nome_metodo)
                                elif nome_metodo in metodos_publicos:
                                    metodos_publicos.remove(nome_metodo)
                                else:
                                    pass
        # Listagem de todos os metodos da classe, sua visibilidade e se foi ou nao utilizada
        for metodos in classe.body:
            if isinstance(metodos, ast.FunctionDef):
                nome_metodo = metodos.name
                if nome_metodo != "__init__":
                    if nome_metodo[0] == "_" and nome_metodo[1] == "_":
                        if nome_metodo not in metodos_privados:
                            print("    Metodo privado --> " + nome_metodo + " (Utilizado)")
                        else:
                            print("    Metodo privado --> " + nome_metodo + " (Nao utilizado)")
                    else:
                        if nome_metodo not in metodos_publicos:
                            print("    Metodo publico --> " + nome_metodo + " (Utilizado)")
                        else:
                            print("    Metodo publico --> " + nome_metodo + " (Nao Utilizado)")
                else:
                    print("    Construtor --> " + nome_metodo)