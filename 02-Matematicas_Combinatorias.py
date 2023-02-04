############# Analisis combinatorio en Python ##################################
## Combinaciones y Permutaciones son escenciales en el estudio de Probabilidades y estadisticas
## En probabilidades cuando trabajamos con distribuciones especiales discretas se utilizan mucho calculos de combinatorias
import math as mt
from scipy.special import perm

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


