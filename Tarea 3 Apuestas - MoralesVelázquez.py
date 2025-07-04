#################
###  OBJETOS  ###
#################

class Jugador :
  def __init__(self, saldo_inicial=100.00) :
    self.saldo = saldo_inicial
    self.rondas = 0

  def apostar_estrategia_maximizar(self, probabilidad: float) :
    from random import random

    if self.saldo <= 0 :
      #print("Saldo agotado.")
      return False

    if random() < probabilidad :
      #print(f"Usted ha ganado {self.saldo} pesos. Su nuevo saldo es: {self.saldo*2} pesos.")
      self.saldo *= 2
    else :
      self.saldo -= self.saldo
      #print(f"Usted ha perdido. Su nuevo saldo es {self.saldo} pesos.")

    return True

  def apostar_estrategia_minimizar(self, probabilidad: float, cantidad_apuesta=50.00) :
    from random import random

    if self.saldo <= 0 :
      #print("Saldo agotado.")
      return False

    if random() < probabilidad :
      self.saldo += cantidad_apuesta
      #print(f"Usted ha ganado {cantidad_apuesta} pesos. Su nuevo saldo es: {self.saldo} pesos.")
    else :
      self.saldo -= cantidad_apuesta
      #print(f"Usted ha perdido. Su nuevo saldo es {self.saldo} pesos.")

    return True
  

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