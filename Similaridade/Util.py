class Util:
    # encontra indice de um objeto em um lista baseado em um campo do objeto
    @staticmethod
    def encontra_indice(metodo_procurado, lista):
        i = 0
        for metodo in lista:
            if metodo_procurado == metodo.nome_metodo:
                return i
            i += 1

    # procura elemento em uma lista baseado em um atributo do objeto
    @staticmethod
    def find(nome_metodo, lista):
        for elemntos in lista:
            if elemntos.nome_metodo == nome_metodo:
                return True
        return False