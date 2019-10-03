'''
Código desenvolvido para disciplina de Arquitetura de Software GCC252

O intuito deste programa eh classificar algum código na linguagem python
em relacao ao seu nivel de coesao. Para isso foi implementado a metrica LCOM4 e 
adicionadas alteracoes extras a metrica original.

Para identificar as pomponentes do programa, transformou-se uma lista que contem
todos os metodos e atributos de uma classe em uma matriz de adjacencia.
Dessa forma, pode-se analisar suas componentes conexas para encontrar
a quantidade de componentes na estrutura e assim poder classificar o
nivel de coesao pela metrica LCOM4. Logo, com o resultado obtido da LCOM4
e verificado qual componente desconexa tem o maior numero de nos. Com esse valor,
é adicionado ao final do valor da LCOM4 a porcentagem que o mesmo represneta referente 
a lista de todos os metodos e atributos. Dessa forma, quanto maior for o numero ao lado
do valor da metrica original, melhor. Pois um valor alto mostra que há um componente
conexo maior, demonstrando uma melhor coesao.

'''

import ast

class LCOM4V2():
    arvore = None
    classe = None
    lista_atributos_e_metodos = []
    qnt_metodos = 0
    matriz_adjacencia = []
    lista_conjuntos = []
    lista_verificacao = []

    def __init__(self, caminho_arquivo_analisado):
        with open(caminho_arquivo_analisado, "r") as codigo_analisado:
            self.arvore = ast.parse(codigo_analisado.read())

        self.reconhecer_classe()
        self.reconhecer_atributos()
        self.reconhecer_metodos()
        print("--------------------------------------------------")
        self.inicializar_matriz_adjacencia()
        self.preencher_matriz_adjacencia()
        self.imprimir_matriz_adjacencia()
        print("--------------------------------------------------")
        self.reconhecer_subgrafos_desconexos()
        self.imprimir_subconjuntos()
        print("--------------------------------------------------")
        self.imprimir_relatorio()

    def reconhecer_classe(self):
        # Identificacao da classe
        for noh in self.arvore.body:
            if isinstance(noh, ast.ClassDef):
                self.classe = noh
                print(self.classe.name)

    def reconhecer_atributos(self):
        # Identificacao dos atributos
        for noh in self.classe.body:
            if isinstance(noh, ast.Assign):
                atributo = noh
                nome_atributo = atributo.targets[0].id
                self.lista_atributos_e_metodos.append(nome_atributo)

    def reconhecer_metodos(self):
        # Identificacao dos metodos
        # Para essa metrica construtores e getters ou setters sao desconsiderados
        for noh in self.classe.body:
            if isinstance(noh, ast.FunctionDef):
                metodo = noh
                if metodo.name != "__init__" and metodo.name[0:3] != "get" and metodo.name[0:3] != "set":
                    self.lista_atributos_e_metodos.append(metodo.name)
                    self.qnt_metodos += 1

    def inicializar_matriz_adjacencia(self):
        # Preparacao da matriz de adjacencia de atributos e metodos
        linha_vazia = [0] * len(self.lista_atributos_e_metodos)
        for linha in range(len(self.lista_atributos_e_metodos)):
            self.matriz_adjacencia.append(linha_vazia.copy())

    def preencher_matriz_adjacencia(self):
        # Identificacao dos acessos aos atributos e chamadas de metodos
        for noh in self.classe.body:
            if isinstance(noh, ast.FunctionDef):
                metodo = noh
                if metodo.name != "__init__" and metodo.name[0:3] != "get" and metodo.name[0:3] != "set":
                    for elemento in ast.walk(metodo):
                        if isinstance(elemento, ast.Attribute):
                            nome_elemento = elemento.attr
                            pos_elemento = self.lista_atributos_e_metodos.index(nome_elemento)
                            pos_metodo = self.lista_atributos_e_metodos.index(metodo.name)
                            # Preenchimento na matriz, considerando o grafo como nao dirigido
                            self.matriz_adjacencia[pos_metodo][pos_elemento] = 1
                            self.matriz_adjacencia[pos_elemento][pos_metodo] = 1

    def imprimir_matriz_adjacencia(self):
        # Impressao da matriz de adjacencia
        for pos in range(len(self.lista_atributos_e_metodos)):
            nome_metodo = str(self.lista_atributos_e_metodos[pos]).ljust(10, " ")
            elementos_alcancados = str(self.matriz_adjacencia[pos])
            print(nome_metodo + " --> " + elementos_alcancados)

    def verificar_relacionamentos(self, elemento, conjunto):
        '''
        Funcao recursiva que analisa cada elemento da lista de metodos e atributos
        Percorre a linha da matriz de adjacencia referente ao elemento passado,
        caso encontrado um relacionamento com outro elemento (aresta do grafo)
        e feita uma chamada recursiva para que que esse outro elemento possa ter seus relacionamentos
        analisados.
        '''
        if elemento not in conjunto:
            conjunto.append(elemento)

        if elemento in self.lista_verificacao:
            self.lista_verificacao.remove(elemento)

        pos_elemento = self.lista_atributos_e_metodos.index(elemento)
        for coluna in range(len(self.lista_atributos_e_metodos)):
            if self.matriz_adjacencia[pos_elemento][coluna] == 1:
                nome_elemento_relacionado = self.lista_atributos_e_metodos[coluna]
                if nome_elemento_relacionado not in conjunto:
                    self.verificar_relacionamentos(nome_elemento_relacionado, conjunto)

    def reconhecer_subgrafos_desconexos(self):
        # Reconhecimento de subgrafos desconexos entre si
        self.lista_verificacao = self.lista_atributos_e_metodos.copy()
        while self.lista_verificacao:
            # Guarda as componentes que tem algum relacionamento
            conj = []
            elemento_qualquer = self.lista_verificacao.pop()
            self.verificar_relacionamentos(elemento_qualquer, conj)
            self.lista_conjuntos.append(conj)

    def imprimir_subconjuntos(self):
        # Impressao dos conjuntos encontrados
        for conjunto in self.lista_conjuntos:
            print(conjunto)

    def percentual_do_maior_conjunto(self):
        '''
        Encontra o subconjunto com maior numero de elementos e calcula o
        percentual deste numero em relacao ao total de elementos, considerando
        todos os conjuntos.
        '''
        max = 0
        for conjunto in self.lista_conjuntos:
            if len(conjunto) > max:
                max = len(conjunto)
        percentual = max/len(self.lista_atributos_e_metodos)
        return round(percentual, 2)

    def imprimir_relatorio(self):
        if self.qnt_metodos == 0:
            lcom4 = 0
            print("Nao ha metodos na classe analisada.")
        elif len(self.lista_conjuntos) == 1:
            lcom4 = 1
            print("Todos os atributos e metodos da classe estao relacionados.")
        else:
            lcom4 = len(self.lista_conjuntos)
            print("A classe pode ser divida em " + str(len(self.lista_conjuntos)) + " novas classes.")

        percentual = self.percentual_do_maior_conjunto()
        print("O maior subconjunto possui " + str(percentual*100) + "% dos elementos da classe.")
        lcom4v2 = lcom4 + percentual
        print("LCOM4V2 = " + str(lcom4v2))


def main():
    LCOM4V2("Exemplo.py")

if __name__ == '__main__':
    main()
