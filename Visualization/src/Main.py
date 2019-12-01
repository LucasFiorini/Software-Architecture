from MontagemDeClasses import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def plotar(lista_classes, largura, espacamento):
    profundidades = []
    alturas = []
    lista_coord_x = []
    x = 0
    #---------------------
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    #---------------------
    for classe in lista_classes:
        profundidades.append(classe["qnt_atributos"])
        alturas.append(classe["qnt_metodos"])
        lista_coord_x.append(x)
        x += espacamento
    #---------------------
    xpos = lista_coord_x
    ypos = len(lista_classes) * [0]
    zpos = len(lista_classes) * [0]
    dx = len(lista_classes) * [largura]
    dy = profundidades
    dz = alturas
    ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color='#00ceaa')
    ax1.set_ylabel("Qnt. Atributos")
    ax1.set_zlabel("Qnt. Metodos")
    plt.show()

lista_classes = montar_classes("Exemplo.py")
plotar(lista_classes, 4, 10)
