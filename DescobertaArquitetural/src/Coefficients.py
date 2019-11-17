class Statistics:
    # a = Número de dependências em ambas as entidades.
    # b = Número de dependências na entidade 1, somente.
    # c = Número de dependências na entidade 2, somente.
    # d = Número de dependências em nenhuma das duas entidades.
    @staticmethod
    def Jaccard(a, b, c):
        return a/(a+b+c)

    @staticmethod
    def generate_values(a, b, c, d):
        print("Jaccard: " + str(Statistics.Jaccard(a, b, c)) + "\n")