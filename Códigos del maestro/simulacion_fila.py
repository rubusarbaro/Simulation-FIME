import scipy.stats as stats;
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kstest

n_clientes = 100 # numero maximo de clientes a atender
min_cliente = 5 # minutos que tarda de llegar un cliente en promedio
media_vent = 8 # media tiempo atencion ventanilla
var_vent= 1    # varianza de tiempo atencion ventanilla
n_ventanillas = 5 # numero de ventanillas

# Set up a helper function for checking p-values against an alpha level, and printing result
def check_p_val(p_val, alpha):

    if p_val < alpha:
        print('We have evidence to reject the null hypothesis.')
    else:
        print('We do not have evidence to reject the null hypothesis.')

# Genera numeros con distribucion exponencial
llegada = stats.expon.rvs(scale=min_cliente, size=n_clientes)
# Genera el tiempo de atencion para cada
t_vent = stats.norm.rvs(loc=media_vent, scale=var_vent, size=n_clientes)


# Dibuja las distribuciones teoricas y esperadas
xs = np.arange(llegada.min(), llegada.max(), 0.1)
fit = stats.expon.pdf(xs, scale=np.mean(llegada))
plt.plot(xs, fit, label='Distribucion Exponencial', lw=3)
plt.hist(llegada, bins=50, density=True, label='Datos Medidos');
plt.legend();
plt.show()

# Hace una prueba estadistica para revisar que los datos encajen 
stat, p_val = kstest(llegada, 'expon', args=(0,5))
print('Statistic: \t{:1.2f} \nP-Value: \t{:1.2e}\n'.format(stat, p_val))
check_p_val(p_val, alpha=0.05)

# Dibuja las distribuciones teoricas y esperadas
xv = np.arange(t_vent.min(), t_vent.max(), 0.1)
fit = stats.norm.pdf(xv, np.mean(t_vent), np.std(t_vent))
plt.plot(xv, fit, label='Distribucion Normal', lw=3)
plt.hist(t_vent, bins=50, density=True, label='Datos Medidos');
plt.legend();
plt.show()

# Hace una prueba estadistica para revisar que los datos encajen
# stat, p_val = normaltest(t_vent)
stat, p_val = kstest(t_vent, 'norm', args=(np.mean(t_vent),np.std(t_vent)))
print('Statistic: \t{:1.2f} \nP-Value: \t{:1.2e}\n'.format(stat, p_val))
check_p_val(p_val, alpha=0.05)

#############################################################################

# Simulacion de ventanillas

# Se reserva memoria para los vectores que se van a utilizar
t_actual = list(range(0, n_ventanillas))  # Tiempo en que las ventanillas estarán libres
t_fila = list(range(0, n_clientes))       # Tiempo que pasan en cliente formado
t_salida = list(range(0, n_clientes))     # Tiempo en que el clientes salio de la ventanilla
n_fila = list(range(0, n_clientes))       # Numero de clientes formados cuando el cliente actual salio de la fila
atendido = list(range(0, n_clientes))     # Ventanilla donde se atendió al cliente

# Actualizacion de tiempos, originalmente "llegada[i]" se generó con una distrubución
# exponencial, por lo que se representan el tiempo que pasó entre la llegada de el
# cliente anterior y este. Al sumarse al cliente anterior obtenemos el tiempo total
# de llegada
for i in range(1, n_clientes):
    llegada[i] = llegada[i] + llegada[i - 1]

# Actualizacion de tiempos iniciales de ventanillas. El "t_actual[i]" representa
# a partir de que momento la ventanilla "i" se desocupada. Todas están desocupadas
# desde el principio.
for i in range(1, n_ventanillas):
    t_actual[i] = 0

# Ciclo principal de la simulacion

# Se procesa cada cliente conformfe fué llegando. Sus tiempos de llegada se calculan arriba
for i in range(0, n_clientes):

    # Hay un pequeño cambio respecto al código visto en clase. Se elige la primera ventanilla
    # (según su numeración) que esté desocupada. Si ninguna está desocupada se elige la que
    # se desocupe antes.
    v_menor = 0
    for j in range(0, n_ventanillas):
        if t_actual[j] <= llegada[i]:
            v_menor = j
            break
        elif t_actual[j] < t_actual[v_menor]:
            v_menor = j

    # Si la ventanilla ya estaba desocupada cuando el cliente llegó, el tiempo de espera es cero.
    # De lo contrario el tiempo de estpera es la diferencia entre el tiempo de llegada del
    # cliente y el tiempo en que se desocupó la ventanilla.
    if (t_actual[v_menor] <= llegada[i]):
        t_fila[i] = 0
    else:
        t_fila[i] = t_actual[v_menor] - llegada[i]

    # Se calculan varios datos de interés de la simulación
    t_salida[i] = llegada[i] + t_fila[i] + t_vent[i]
    t_actual[v_menor] = t_salida[i]
    atendido[i] = v_menor

# Se calculan cuantas personas estaban formadas al momento de que un cliente sale de la fila para
# entrar en la ventanilla. Este código solo funciona si hay una sola fila. Esta parte se cambió
# de lo visto en clase, pues en la clase se tomaba la información cuendo el cliente salía de la
# ventanilla, mientras que ahora toma la información cuando el cliente sale de la fila.
j = 0
for i in range(0, n_clientes):
    j = i + 1
    while j < n_clientes and llegada[j] < t_fila[i] + llegada[i]:
        j = j + 1
    n_fila[i] = j - i
    if n_fila[i] == 1 and t_fila[i] == 0:
        n_fila[i] = 0

print("Tiempo de llegada\tTiempo en fila\tTiempo de salida\tClientes en espera\tAtendido en")

for i in range(0, n_clientes):
    print(f"{llegada[i]:.2f}\t\t\t{t_fila[i]:.2f}\t\t{t_salida[i]:.2f}\t\t\t{n_fila[i]}\t\t\t{atendido[i]}")
