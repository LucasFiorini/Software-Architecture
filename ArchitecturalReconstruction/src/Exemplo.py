class Util:
    def printar():
        print("oitoportas")

    def calcular():
        print("um mais um")

    def abrir():
        print("abre alguma coisa")


class Terminal:
    def cd():
        Util.printar()

    def ls(self):
        self.cd()
        print("conteudo da pasta")

class Bash:
    def man():
        Util.calcular()


class Shell:
    def grep():
        Util.abrir()