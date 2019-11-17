class Teste:

	def faz_algo(self):
		if 1 == 1:
			print("um é igual a 1 cara")
		elif 'a' == 'b':
			print("pois eh cara")
		else:
			print("sei nao")
		if 1 > 2:
			Oi.metodo_1()
			print("carai mane")
		print("eae")

	def printa_os_teste(self):
		for i in range(30):
			print("oh os teste ai!")

	def recebe_os_trem(self):
		nome = input("fala seu nome ai cumpadi")
		Util.fala_oi()
		Util.fala_oi()
		Util.fala_oi()
		print(nome)

class Util:

	def fala_oi(self):
		print("oi meu bacano ")

	def conta_cafe(self):
		i = 0
		t = Teste()
		t.faz_algo()
		Teste.faz_algo()
		while i < 10:
			print(i + "cafes!")

	def abre_os_arquivao_top(self):
		Oi.metodo_1()
		f = open("arquivao.txt", 'r')

	def tenta_algo(self):
		try:
			print("tentando aqui...")
		except:
			pass


class Oi:

	def metodo_1(self):
		pass

	def metodo_2(self):
		pass


class Agua:
	def priemiro(self):
		Oi.metodo_1()
		Oi.metodo_2()

	def segundo(self):
		Util.fala_oi()


class Pedra:
	def terceira(self):
		Oi.metodo_1()
		Oi.metodo_2()

	def quarta(self):
		Util.fala_oi()



class DataBase:
	def con(self):
		Teste.recebe_os_trem()
		Teste.printa_os_teste()

	def close_conn(self):
		Oi.metodo_1()

class read_csv:

	def read(self):
		Oi.metodo_1()
		pass

	def write(self):
		pass

class Find:
	@staticmethod
	def encontra_indice(metodo_procurado, lista):
		i = 0
		for metodo in lista:
			if metodo_procurado == metodo.nome_metodo:
				return i
		i += 1

	@staticmethod
	def find(nome_metodo, lista):
		for elemntos in lista:
			if elemntos.nome_metodo == nome_metodo:
				return True
		return False


class List:
	def find_element(self):
		Find.encontra_indice()
		Find.find()
	def insere(self):
		pass

class Stack:
	def find_stack_element(self):
		Find.find()
	def insert(self):
		Find.find()