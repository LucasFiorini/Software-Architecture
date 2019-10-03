
class Pipe:
    def escrever(self):
        f = open("guru99.txt", "w+")
        for i in range(10):
            f.write("This is line %d\r\n" % (i + 1))
            f.close()

    def escrever_data(self, data):
        f = open("guru99.txt", "w+")
        f.write(data)
        f.close()

class Pump:
    def get_data(self):
        print("type your option")
        input()
        Pipe.escrever_data()

class Filter():
    #processamento
    Pipe.escrever()

class Filter1():
    #processamento
    Pipe.escrever()


class Filter11():
    #processamento
    Pipe.escrever()


class Sink:
    def display_data(self):
        print("I'm some data")

    def ler(self):
        f = open("guru99.txt", "r")
        content = f.read()
        print(content)