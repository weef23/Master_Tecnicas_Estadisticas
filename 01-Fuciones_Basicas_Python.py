############### Python nos provee una serie de funciones basicas para trabajar con Datos Estadisticos

####################### PARTE 1 FUNCIONES MATEMATICAS  BASICAS #########################################
## La fucnon Math nos provee una serie de funciones utililes
import math as mt

### Constantes en Python
pi = mt.pi ## Retorna el numero pi
print(f"El valor de pi es {pi}")
infinito = mt.inf ## Nos devuelve el numero
print(f"El valor de infinito es {infinito}")
e = mt.e
print(f"El valor de e {e}")
tau = mt.tau ## Constante Tau
## Python tambien nos provee la constante null la cual es muy util
## En representacion de un valor faltante.
null = mt.nan
print(f"El valor null es {null}")

### Funciones Exponenciales y logaritmicas
x = 2
y = 3
## La funcion pow nos permite elevar una potencia x elvado a la y
potencia = mt.pow(2, 3)
print(f"El valor de {x} elevado a la {y} es {potencia}")
### La funcion logaritmo nos devuelve el logaritmo natural de un numero
lg = mt.log(x) ## Logaritmo de base e
print(f"El logaritmo de x en base e es {lg}")

lgy = mt.log(x, y) ## Logaritmo de base x en base e
print(f"El logaritmo de x en base y es {lgy}")

### Funciones Trigonometricas en Python

## Funcion del Seno y el Coseno
seno = mt.sin(mt.pi) ## Seno de PI
coseno = mt.cos(mt.pi)
print(f"El seno de PI es {seno} y el coseno es {coseno}")

## Funciones Tangente
tan = mt.tan(mt.pi/2) ## Tangente de 90 grados en radianes
## En realidad esto deberia tender al infinito pero por el numero de decimales estamos obtiendo un valor cercano a 0
print(f"La tangente de pi/2 es {tan}")
## Estas funciones por defecto reciben su argumento en radianes y no en grado
## De la siguiente forma podemos convertir grados a radianes y viceversa

angulo_radianes = mt.radians(45) ## Convertimos 45 grados a radianes
print(f"45 grados en radianes es {angulo_radianes}")
angulo_grados =  mt.degrees(0.7853981633974483) ## Conversion de rad a grados.



