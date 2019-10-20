from Similaridade import Similaridade

def main():
    g = Similaridade("exemplo.py")
    print(g.lista_info_classes[0].metodos_externos[0].nome_metodo)
    print(g.lista_info_classes[0].metodos_externos[0].vezes_chamado)


if __name__ == '__main__':
    main()

#TODO
# arrumar contagem de prints que estao dentro de if/else pois ele os desconsidera
# inventar alguma metrica para as informações coletadas
# tentar separar as classes em MVP
# interface de escolha para o usuário entre comprar uma classe com todas, duas especificas ou todas com todas
