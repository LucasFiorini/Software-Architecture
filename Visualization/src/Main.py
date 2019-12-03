from MontagemDeClasses import *
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cm as cm

def plotar(lista_classes, largura, espacamento):
    profundidades = []
    alturas = []
    lista_coord_x = []
    labels = []
    xs = []
    x = 0
    #---------------------
    fig = plt.figure()
    ax1 = fig.add_subplot(111, projection='3d')
    #---------------------
    for classe in lista_classes:
        profundidades.append(classe["qnt_atributos"])
        alturas.append(classe["qnt_metodos"])
        lista_coord_x.append(x)
        labels.append(classe["nome"])
        x += espacamento
    #---------------------
    xpos = lista_coord_x
    ypos = len(lista_classes) * [0]
    zpos = len(lista_classes) * [0]
    dx = len(lista_classes) * [largura]
    dy = profundidades
    dz = alturas

    xlabels = np.array(labels)

    ax1.w_xaxis.set_ticks(xpos)
    ax1.w_xaxis.set_ticklabels(xlabels)
    colors = cm.rainbow(np.linspace(0,1,len(ypos)))

    ax1.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, alpha = 0.5)

    ax1.set_xlabel("Nome das Classes")
    ax1.set_ylabel("Qnt. Atributos")
    ax1.set_zlabel("Qnt. Metodos")

    plt.show()

lista_classes = montar_classes("Exemplo.py")
plotar(lista_classes, 4, 10)
