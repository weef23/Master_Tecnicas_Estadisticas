############################ DISTRIBUCIONES ESPECIALES DISCRETAS #######################################
from numpy import random
import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt
### Distribucion de Bernoulli, Es una distribucion discreta cuya variable objetivo tiene unicamente 2 valores
### Estos valores representan si es o no probable que el suceso ocurra. Probabilidad de exito P(Z=1) = p
### La probabilidad de No exito P(Z=0) = 1 - p,

### La libreria random nos permite generar una matriz de 10 valor
matriz = random.binomial(n=10, p=0.25, size=10)
## Cada valor de la matriz representa el numero de exitos experimentados en 10 ensayos
## con una probabilidad de exito del 0.25
print(f"La matriz binomial es {matriz}")
#### Graficando la distribucion binomial
N = 40 ## Numero de elementos en la poblacion
p = 0.4 ## Probabilidad de exito.
### Distribucion de probabilidad

### Funcion de masa de probabilidad
binomial = binom(N, p)

## Generamos la distribucion binomial
x = np.arange(binomial.ppf(0.01), binomial.ppf(0.99))
## Funcion de masa de probabilidad
fmp = binomial.pmf(x)

### Grafica de la distribucion de probabiliadad Binomial
plt.plot(x, fmp, '--')
plt.vlines(x, 0, fmp, colors='b', lw=5, alpha=0.5)
plt.title('Distribución Binomial')
plt.ylabel('probabilidad')
plt.xlabel('valores')
plt.show()
#### En el siguiente ejemplo proceder a calcular los primero cuatro momentos mean, variance, skewness, and kurtosis
n, p = 5, 0.4
mean, var, skew, kurt = binom.stats(n, p, moments='mvsk')
### Matriz de distribucion de probabilidad
x = np.arange(binom.ppf(0.01, n, p), binom.ppf(0.99, n, p))
fig, ax = plt.subplots(1, 1)
ax.plot(x, binom.pmf(x, n, p), 'bo', ms=8, label='binom pmf')
ax.vlines(x, 0, binom.pmf(x, n, p), colors='b', lw=5, alpha=0.5)

## Alternativamente, se puede llamar al objeto de distribución (como una función)
## para fijar la forma y la ubicación. Esto devuelve un objeto RV "congelado"
## que mantiene fijos los parámetros dados
rv = binom(n, p)
ax.vlines(x, 0, rv.pmf(x), colors='k', linestyles='-', lw=1, label='frozen pmf')
ax.legend(loc='best', frameon=False)
plt.show()