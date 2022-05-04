import time
import random
from utilities import *
from algoritms import BruteForcecutrod
def main():
    p=[]
    temp=[]
    stp=base(5, 30, 5) # NUMERO DE BARRAS: [CUANTO MIDE PRIMER BARRA][CUANTO MIDE ULTIMA BARRA][EN CUANTO AUMENTA CADA BARRA]
    for i in stp:
        p = creationRot(i) #GENERA MEDIDAS Y GANANCIAS DE LAS BARRAS EN AUTOMATICO(se puede modificar en utiles.py)
        start = time.time()
        BruteForcecutrod(p,i-1 )#P ES LA BARRA A MEDIR,i-1 ES R
        finish = time.time()
        total = finish- start
    graph(stp, temp)
main()                     
