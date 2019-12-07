from Refatorador import Refatorador

ref = Refatorador("Exemplo.py")
ref.remover_metodo("m1", "C1")
ref.injetar_metodo("Animal")
ref.escrever_novo_codigo_no_arquivo("ExemploNOVO.py")
