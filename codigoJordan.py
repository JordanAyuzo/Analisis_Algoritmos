
import random
import time
import matplotlib.pyplot as plt
from random import randint
#UTILERIA
def creationReverse(x):
    a = []
    i = 0
    for i in range(1,x+1):
        a.append(x-i)
    return a
def creation(x):
    a = []
    i = 0
    for i in range(x):
        a.append(i)
    return a
def base(ini,x,stp):
    a = []
    i = 0
    for i in range(ini,x+1,stp):
        a.append(i)
    return a
#GRAFICAR
def graficar(x,m,q):
    #m,p y r son el tiempo y x es el numero de variables
    plt.plot(x,m, label = "Merge")
    plt.plot(x,q,label = "Quick")
    plt.legend()
    plt.title ('Merge VS Quick de '+ str(x[len(x)-1]) +' Datos', fontsize= 12)
    plt.xlabel("Numero de Variables", fontsize=10)
    plt.ylabel("Tiempo de Ejecución", fontsize=10)
    plt.grid()
    plt.show()
# METODO DE ORDENAMIENTO MERGE
        #solo te pide el arr
def merge_sort(array, left_index, right_index):
    if left_index >= right_index:
        return

    middle = (left_index + right_index)//2
    merge_sort(array, left_index, middle)
    merge_sort(array, middle + 1, right_index)
    merge(array, left_index, right_index, middle)

def merge(array, left_index, right_index, middle):
    # Make copies of both arrays we're trying to merge

    # The second parameter is non-inclusive, so we have to increase by 1
    left_copy = array[left_index:middle + 1]
    right_copy = array[middle+1:right_index+1]

    # Initial values for variables that we use to keep
    # track of where we are in each array
    left_copy_index = 0
    right_copy_index = 0
    sorted_index = left_index

    # Go through both copies until we run out of elements in one
    while left_copy_index < len(left_copy) and right_copy_index < len(right_copy):

        # If our left_copy has the smaller element, put it in the sorted
        # part and then move forward in left_copy (by increasing the pointer)
        if left_copy[left_copy_index] <= right_copy[right_copy_index]:
            array[sorted_index] = left_copy[left_copy_index]
            left_copy_index = left_copy_index + 1
        # Opposite from above
        else:
            array[sorted_index] = right_copy[right_copy_index]
            right_copy_index = right_copy_index + 1

        # Regardless of where we got our element from
        # move forward in the sorted part
        sorted_index = sorted_index + 1

    # We ran out of elements either in left_copy or right_copy
    # so we will go through the remaining elements and add them
    while left_copy_index < len(left_copy):
        array[sorted_index] = left_copy[left_copy_index]
        left_copy_index = left_copy_index + 1
        sorted_index = sorted_index + 1

    while right_copy_index < len(right_copy):
        array[sorted_index] = right_copy[right_copy_index]
        right_copy_index = right_copy_index + 1
        sorted_index = sorted_index + 1
###############################
def mergeSort2(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        mergeSort2(L)
        mergeSort2(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
# METODO DE ORDENAMIENTO QUICK
        # Te pide (lista , 0, tamaño de lista) 
def quicksort(arr, start , stop):
    if(start < stop):
        pivotindex = partitionrand(arr,\
                             start, stop)
        quicksort(arr , start , pivotindex-1)
        quicksort(arr, pivotindex + 1, stop)
def partitionrand(arr , start, stop):
    randpivot = random.randrange(start, stop)
    arr[start], arr[randpivot] = \
        arr[randpivot], arr[start]
    return partition(arr, start, stop)
def partition(arr,start,stop):
    pivot = start 
    i = start + 1
    for j in range(start + 1, stop + 1):

        if arr[j] <= arr[pivot]:
            arr[i] , arr[j] = arr[j] , arr[i]
            i = i + 1
    arr[pivot] , arr[i - 1] =\
            arr[i - 1] , arr[pivot]
    pivot = i - 1
    return (pivot)
 
#La carga de funciones 
def main():
    m=[]
    q=[]
    maxvar = int(input("Elije el numero maximo de n: "))
    stp = int(input("Elije el paso que debe llevar: "))
    cant = base(stp,maxvar,stp)
    i = 0
    for i in cant:
        lista1 =creation(i)
        random.shuffle(lista1)
        lista2=lista1
        ##########
        start = time.time()
        quicksort(lista2,0,i-1)
        finish = time.time()
        total = finish- start
        q.append(total)
        ##############
        start = time.time()
        merge_sort(lista1,0, i-1)
        mergeSort2(lista1)
        finish = time.time()
        total = finish- start
        m.append(total)
        ###########
        print(i)
    print(cant)
    print(m)
    print(q) 
    graficar(cant, m, q)
main()

