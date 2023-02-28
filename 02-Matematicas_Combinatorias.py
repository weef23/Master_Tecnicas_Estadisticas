############# Analisis combinatorio en Python ##################################
## Combinaciones y Permutaciones son escenciales en el estudio de Probabilidades y estadisticas
## En probabilidades cuando trabajamos con distribuciones especiales discretas se utilizan mucho calculos de combinatorias
import math as mt
from scipy.special import perm
from scipy.special import comb
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
## Sin embargo que pasa si queremos calcular el numero de repeticiones por cada elemento.
## Python como tal Python no nos proporciona una funcion para calcular permutaciones con repeticion pero
## Podemos partir de la siguiente formula Pa,b,c.... = n!/a!b!c!....
## Donde n es el numero de observaciones a el numero de veces que aparece el elemento a, b el numero de elementos que
## Aparece b y c el numero de veces que aparece c

### Pasamos el numero de elementos y un parametro que corresponde a una lista dinamica
def permutacione_con_repeticion(n, *elemetos):
    ### La productoria de los factoriales de cada elemento corresponde al denominador de la formula
    ### Basicamente es la multiplicacion de cada uno de los factoriales de cada elemento
    productoria = 1
    for i in elemetos:
        productoria *= mt.factorial(i)

    return mt.factorial(n)/productoria

## Ahora probamos la funcion calculando el numero de palabras que podemos crear con la palabra BANANA
b = 1 ## Representa el numero de veces en que aparece la letra b
a = 3 ## Representa el numero de veces que aparece la letra a
c = 2 ## Representa el numero de veces que aparece la letra n
n = 6 ## representa el numero total de observaciones

nPabc = permutacione_con_repeticion(n, a, b, c)
print(f"El numero de palabras a formar con la palabra Banana es : {nPabc}")

#### USO DE COMBINACIONES EN PYTHON, Las combinaciones en Python corresponden al numero de subconjuntos que podemos
#### Generar con los elementos de un conjuntos, en Estadistica se utilizan como coeficientes binomiales en la
### Mayoria de distribuciones discretas nCm se describe mediante la formula  n!/m!(n!-m!)

## Con la siguiente funcion podemos calcular la combinacion de nCm
combinacion_count = lambda n, m: mt.factorial(n)//(mt.factorial(m) * mt.factorial(n-m))

#### Calculamos 4C2
comb1 = combinacion_count(4,2)
print(f"La combinacion de 4, 2 es {comb1}")

### La libreria scipy tambien nos proporociona un metodo para calcular las combinatorias entre elementos
print(f"La combinacion de 4, 2 es {comb(4,2, exact=True)}")

## Si usamos el parametro true nos traera las combinaciones con repeticion lo cual es particularmente interesante
print(f"La combinacion con repeticion de 4C2 es {comb(4, 2, exact=True, repetition=True)}")

### Tambien es posible generar las combinaciones a partir de una lista, lo que resultaria particularmente util
## Usando la lista l que definimos para la generacion de permutaciones a partir de una lista

## Estamamos generando los conjuntos de 2 elementos que podemos formar con l
comb_list = list(itertools.combinations(l, 2))
print(comb_list)

## Si los queremos con repeticion entonces podemos usar esta funcion de itertools
comb_list_rep = list(itertools.combinations_with_replacement(l, 2))
print(comb_list_rep)

pos = ['C', 'T']
comb_list_rep = list(itertools.combinations_with_replacement(pos, 3))
print(comb_list_rep)

