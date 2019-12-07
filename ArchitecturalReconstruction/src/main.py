from Reconstrutor import *
from Refatorador import Refatorador

def main():
    a = Reconstrutor()
    mudancas = a.encontrar_uso_util()

    ref = Refatorador("Exemplo.py")

    for move_method in mudancas.keys():
        ref.remover_metodo(mudancas[move_method], "Util")
        ref.injetar_metodo(move_method)
        ref.escrever_novo_codigo_no_arquivo("ExemploNOVO.py")

if __name__ == '__main__':
    main()