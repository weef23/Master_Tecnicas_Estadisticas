############# Analisis combinatorio en Python ##################################
## Combinaciones y Permutaciones son escenciales en el estudio de Probabilidades y estadisticas
## En probabilidades cuando trabajamos con distribuciones especiales discretas se utilizan mucho calculos de combinatorias
import math as mt
from scipy.special import perm
import itertools

### Lo primero que debemos aprender en Matematicas combinatorias es el calculo del Factorial, para ellos usamos
### la funcion Factorial que nos proporciona la libreria math en Python

fact_5 = mt.factorial(5)
print(f"El Factorial del 5 es {fact_5}")
fact_0 = mt.factorial(0)
print(f"Factorial de 0 es {fact_0}")
#######################################################################################################################
## Permutaciones corresponde al numero de ordenaciones que podemos obtener de una sucesion de elementos ya sea que este
## Ordenadas o no la formula de las permutaciones es P = m!/(m-n)! esta formula nos devuelve el numero de grupos que
## Podemos obtener con un determinado conjunto m vendria a ser el tamaño del conjunto y n el numero de elementos del
## conjunto, esto es si aumimos que es una permutacion sin repeticion es decir que en cada orden cada elemento aparece
## Una vez

permt = lambda  m, n : mt.factorial(m)//mt.factorial(m-n)

## De cuantas formas podemos ordenar los numeros del 1 al 5 de tal forma que formen numeros de 4 digitos
permutacion = permt(5,4)
print(f"El numero de ordenaciones es {permutacion}")
### Si m=n entonces simplermente calculamos el factorial
permutacion = mt.factorial(5)
print(f"El Numero de formas en que podemos ordenar un elemento es {permutacion}")
## La Biblioteca scipy nos provee de perm la cual nos permite hacer exactamente lo mismo que hicimos con la funcion
## Lambda anteriormente mencionada.
prm = perm(4, 2)
print(f"La permutacion 4P2 es {prm} ")
## Nos devuelve un valor entero
prm = perm(4, 2, exact=True)
print(f"La permutacion 4P2 es {prm} ")

## El caso m=n
perm = perm(4, 4, exact=True)
fact = mt.factorial(4)
print(f"Cuando m=n 4P4 la permutacion {perm} es el factorial {fact}")

### Python tambien nos permiten generar permutaciones a traves de una lista con la libreria itertools

## Definimos una lista de elementos
l = ['a', 'b', 'c', 'd']
## A continuacion generamos el numero de ordenaciones que podemos obtener las permutacion de 2 elementos
p_list = list(itertools.permutations(l, 2))
print(p_list)
## Con 3 elementos
p_list3 = list(itertools.permutations(l, 3))
print(p_list3)
## Con m = n
p_list4 = list(itertools.permutations(l, 4))
print(p_list4)

## Anteriormente abarcamos las repeticiones con combinacion ahora abordaremos las repeticiones sin combinaciones