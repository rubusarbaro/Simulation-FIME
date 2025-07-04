#################
###  OBJETOS  ###
#################

class Jugador :
  """
  Clase Jugador, que representa a un jugador que va a apostar.

  Args:
    saldo_inicial (float): Saldo con el que el Jugador comienza la primera apuesta. Por defecto es 100.00.
  """
  def __init__(self, saldo_inicial=100.00) :
    self.saldo = saldo_inicial  # Saldo inicial del Jugador. Por defecto es 100.00, como en el ejercicio.

  def apostar_estrategia_maximizar(self, probabilidad: float) :
    """
    La estrategia «maximizar» consiste en apostar todo el dinero disponible. Si el jugador gana, duplica su apuesta, de lo contrario, la pierde.

    Args:
      probabilidad (float): Probabilidad de que el Jugador gane la apuesta.
    """
    from random import random

    if self.saldo <= 0 :  # Revisa si el jugador cuenta con saldo suficiente.
      #print("Saldo agotado.")
      return False  # Si no cuenta con saldo, retorna False, por lo que finaliza el juego.

    if random() < probabilidad :  # Genera un número aleatorio entre 0 y 1, si el número generado es menor a la probabilidad establecida, el jugador ha ganado.
      #print(f"Usted ha ganado {self.saldo} pesos. Su nuevo saldo es: {self.saldo*2} pesos.")
      self.saldo *= 2 # Si el jugador gana, duplica su saldo.
    else :
      self.saldo -= self.saldo  # Si el jugador pierde, le retira su apuesta (en este caso, todo su saldo).
      #print(f"Usted ha perdido. Su nuevo saldo es {self.saldo} pesos.")

    return True # Retorna True, lo que significa que el Jugador sí tenía saldo cuando empezó la apuesta.

  def apostar_estrategia_minimizar(self, probabilidad: float, cantidad_apuesta=5.00) :
    """
    La estrategia «minimizar» consiste en apostar una pequeña cantidad de dinero. Si el jugador gana, duplica su apuesta, de lo contrario, la pierde.

    Args:
      probabilidad (float): Probabilidad de que el Jugador gane la apuesta.
      cantidad_apuesta (float): Cantidad mínima que el jugador va a apostar. Por defecto es 5.00, como lo establece el ejercicio del MIT.
    """
    from random import random

    if self.saldo < cantidad_apuesta :  # Verifica que el usuario tenga saldo suficiente.
      #print("Saldo insuficiente.")
      return False  # Si el usuario no cuenta con saldo suficiente, finaliza la apuesta.

    if random() < probabilidad :  # Genera un número aleatorio entre 0 y 1, si el número generado es menor a la probabilidad establecida, el jugador ha ganado.
      self.saldo += cantidad_apuesta  # Si el jugador gana, duplica su apuesta, sumando solamente la cantidad que apostó, ya que no se descuenta del saldo al principio.
      #print(f"Usted ha ganado {cantidad_apuesta} pesos. Su nuevo saldo es: {self.saldo} pesos.")
    else :
      self.saldo -= cantidad_apuesta  # Si el jugador pierde, se retira de su saldo la cantidad que apostó.
      #print(f"Usted ha perdido. Su nuevo saldo es {self.saldo} pesos.")

    return True # Retorna True, lo que significa que el Jugador sí tenía saldo cuando empezó la apuesta.
  

####################
###  PARÁMETROS  ###
####################

p = 0.8
objetivo = 1000.00


###################
###  EJECUCIÓN  ###
###################

### Estrategia MAXIMIZAR ###
jugador_1 = Jugador() # Juega estrategia de maximizar
juegos_1 = 0

for i in range(1000) :

  while jugador_1.apostar_estrategia_maximizar(p) and jugador_1.saldo < objetivo :
    pass

  if jugador_1.saldo >= objetivo :
    juegos_1 += 1

  jugador_1.saldo = 100.00

print(f"Probabilidad de ganar: {juegos_1/1000}")

### Estrategia MINIMIZAR ###
jugador_2 = Jugador() # Juega estrategia de minimizar
juegos_2 = 0

for i in range(1000) :

  while jugador_2.apostar_estrategia_minimizar(p) and jugador_2.saldo < objetivo :
    pass

  if jugador_2.saldo >= objetivo :
    juegos_2 += 1

  jugador_2.saldo = 100.00

print(f"Probabilidad de ganar: {juegos_2/1000}")