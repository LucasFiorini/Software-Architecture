class Teste:

	def faz_algo(self):
		if 1 == 1:
			print("um é igual a 1 cara")
		elif 'a' == 'b':
			print("pois eh cara")
		else:
			print("sei nao")
		if 1 > 2:
			print("carai mane")
		print("eae")

	def printa_os_carai(self):
		for i in range(30):
			print("oh os carai ai!")

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
		while i < 10:
			print(i + "cafes!")

	def abre_os_arquivao_pika(self):
		f = open("arquivao.txt", 'r')

	def tenta_algo(self):
		try:
			print("tentando aqui...")
		except:
			pass
