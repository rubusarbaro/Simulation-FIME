###################
###  FUNCIONES  ###
###################

def simular_asientos(personas: int, repeticiones: int) :
  """
  Función que permite obtener la probabilidad promedio de un juego de sillas repetido n veces. Mide la probabilidad de que una persona se siente en su lugar original.

  Args:
    personas (int): Cantidad de personas en el juego.
    repeticiones (int): Cantidad de veces a simular el juego, con el fin de obtener un promedio.
  """
  from random import shuffle
  from statistics import mean

  lista_personas = [n for n in range(1,personas + 1)]   # Lista de personas. Las personas son representadas por un número del 1 a la cantidad de personas fijada.

  lista_probabilidades = [] # Lista donde se almacenan las probabilidades a promediar.

  for i in range(repeticiones):     # Bucle for que repite el juego n veces.
    asientos_revueltos = lista_personas.copy()  # Crea una copia de las personas, con el fin de que la original no se vea afectada.
    shuffle(asientos_revueltos) # Revuelve la lista de personas.

    counter = 0 # Contador de personas en el mismo asiento

    for j in range(len(lista_personas)):
      if asientos_revueltos[j] == lista_personas[j]:    # Compara la posición de cada persona en la lista original y la lista copiada.
        counter += 1

    lista_probabilidades.append(counter/personas)   # Obtiene la probabilidad y la agrega a la lista de probabilidad.

  return mean(lista_probabilidades) # Retorna el promedio de las probabilidades en una escala de 0 a 1.


###################
###  EjECUCIÓN  ###
###################
# Parámetros: 100 personas; 1000 repeticiones.

print(f" Probabilidad: {simular_asientos(100,1000)}")