import time
from utilities import *
from algoritms import BottomUpCutRod
def test():
    p=[0,1,5,8,9,10,17,17,20,24,30]
    print(BottomUpCutRod(p, 4))
def main():
    p=[]
    temp=[]
    stp=base(5, 20, 5)# NUMERO DE BARRAS: [CUANTO MIDE PRIMER BARRA][CUANTO MIDE ULTIMA BARRA][EN CUANTO AUMENTA CADA BARRA]
    for i in stp:
        p = creationRot(i)
        start = time.time()#GENERA MEDIDAS Y GANANCIAS DE LAS BARRAS EN AUTOMATICO(se puede modificar en utiles.py)
        BottomUpCutRod(p,i-1 )#P ES LA BARRA A MEDIR,i-1 ES R
        finish = time.time()
        total = finish- start
        temp.append(total)
    graph(stp, temp)
main()