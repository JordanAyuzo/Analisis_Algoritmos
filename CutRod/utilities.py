import random
import matplotlib.pyplot as plt
def creationRot(x):
    a = []
    #a.append(0)
    i = 0
    for i in range(x+1):
        #num = random.randint(1, 300)
        a.append(i)
    return a
def base(ini,fin,stp):
    a = []
    i = 0
    for i in range(ini,fin+1,stp):
        a.append(i)
    return a
def graph(var,temp):
    plt.plot(var,temp,label = "")
    plt.legend()
    plt.title ('Grafica '+ str(var[len(var)-1]) +' Datos', fontsize= 12)
    plt.xlabel("Numero de Variables", fontsize=10)
    plt.ylabel("Tiempo de Ejecución", fontsize=10)
    plt.grid()
    plt.show()