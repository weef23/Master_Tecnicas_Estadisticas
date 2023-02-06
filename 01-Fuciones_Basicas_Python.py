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

###################### OTRAS FUNCIONES EN PYTHON ###############################
modulo = mt.fmod(3,2) ### El modulo o residuo de la division
print(f"El modulo de la division entre 3 y 2 es {modulo}")
cociente = mt.remainder(3,4) ## Esta funcion nos devuelve el cociente entero de la division
print(f"El cociente entero de la division entre 3 y 2 es {cociente}")
mdf = mt.modf(3.25) ## Separa el entero de los decimales
print(f"El resultado es {mdf}")
redinf = mt.floor(3.26) ## Redondea al entero mas bajo
print(f"El resultado es {redinf}")
redondeo = mt.ceil(3.26) ## Redondeo hacia arriba
print(f"El resultado es {redondeo}")
gcd = mt.gcd(24,36) ## Maximo comun divisor entre dos numeros
print(f"El resultado es {gcd}")
############### Funciones para comprobar numero #################
print(f"El mumero 2.5 es finito? {mt.isfinite(2.5)}")
print(f"El mumero 2.5 es infinito? {mt.isinf(2.5)}")
print(f"El numero es nan? {mt.isnan(3)}")
## En computacion cuando trabajamos con numeros decimales trabajamos con aproximaciones
## Es realmente la raiz cuadrada de 2 elevado al cuadrado 2? no realmente pero
## Con la funcion isclose podemos medir si se aproxima o no, esto es util con valores continuos.
print(f"Es la raiz cuadrada de 2 elevado al cuadrado 2? {mt.isclose(mt.sqrt(2)**2,2,rel_tol=1e-09)}")
