class Statistics:
    # a = Número de dependências em ambas as entidades.
    # b = Número de dependências na entidade 1, somente.
    # c = Número de dependências na entidade 2, somente.
    # d = Número de dependências em nenhuma das duas entidades.
    a = 0
    b = 0
    c = 0
    d = 0

    def Jaccard(self,a,b,c):
        return a/(a+b+c)

    def simpleMatching(self,a,b,c,d):
        return (a+d)/(a+b+c+d)

    def Yule(self,a,b,c,d):
        return (a*d - b*c)/(a*d + b*c)    
    
    def Hamann(self,a,b,c,d):
        return ((a+d)-(b+c))/((a+d)+(b+c))
    
    def Sorenson(self,a,b,c):
        return (2*a)/(2*a+b+c)
    
    def RogersAndTanimoto(self,a,b,c,d):
        return (a+d)/(a+2*(b+c)+d)
    
    def SokalAndSneath(self,a,b,c,d):
        return 2*(a+d)/(2*(a+d)+b+c)
    
    def RusselAndRao(self,a,b,c,d):
        return a/(a+b+c+d)
    
    def DotProduct(self,a,b,c):
        return a/(b+c+2*a)
    
    def SokalAndSneath2(self,a,b,c): 
        return a/(a+2*(b+c))
    
    def generateValues(self,a,b,c,d):
        print("Jaccard: " + str(self.Jaccard(a,b,c)) + "\n")
        print("Simple Matching: " + str(self.simpleMatching(a,b,c,d)) + "\n")
        print("Yule: " + str(self.Yule(a,b,c,d)) + "\n")
        print("Hamann: " + str(self.Hamann(a,b,c,d)) + "\n")
        print("Sorenson: " + str(self.Sorenson(a,b,c)) + "\n")
        print("Rogers and Tanimoto: " + str(self.RogersAndTanimoto(a,b,c,d)) + "\n")
        print("Sokal and Sneath: " + str(self.SokalAndSneath(a,b,c,d)) + "\n")
        print("Russel and Rao: " + str(self.RusselAndRao(a,b,c,d)) + "\n")
        print("Dot-product: " + str(self.DotProduct(a,b,c)) + "\n")
        print("Sokal and Sneath 2: " + str(self.SokalAndSneath2(a,b,c)) + "\n")
        print("Observação: Hamann e Yule têm um intervalo entre -1 e 1.")
        print("Todos os outros coeficientes possuem um intervalo entre 0 e 1.")

    def __init__(self):
        print("Insira os valores de a,b,c e d: ")
        print("a = Número de dependências em ambas as entidades.")
        print("b = Número de dependências na entidade 1, somente.")
        print("c = Número de dependências na entidade 2, somente.")
        print("d = Número de dependências em nenhuma das duas entidades.")
        self.a = int(input())
        self.b = int(input())
        self.c = int(input())
        self.d = int(input())

aux = Statistics()
aux.generateValues(aux.a, aux.b, aux.c, aux.d)