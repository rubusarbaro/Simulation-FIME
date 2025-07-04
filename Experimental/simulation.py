import entidades
import simpy

env = simpy.Environment()

def generar_clientes(cantidad_clientes: int, probabilidad_clientes_observadores: float) :
    from random import random

    lista_clientes = []

    for i in range(cantidad_clientes) :
        tipo_cliente = "observador" if random() < probabilidad_clientes_observadores else "regular"
        lista_clientes.append(entidades.Cliente(env, tipo_cliente))

    return lista_clientes

def generar_cajeros(cantidad_cajeros: int, probabilidad_cajeros_rápidos: float) :
    from random import choice,random

    lista_cajeros = []

    for i in range(cantidad_cajeros) :
        r = random()

        if r < probabilidad_cajeros_rápidos :
            velocidad_cajero = choice([0.1,0.2,0.3])
        elif r < probabilidad_cajeros_rápidos + ((1 - probabilidad_cajeros_rápidos) / 2) :
            velocidad_cajero = choice([0.4,0.5])
        else :
            velocidad_cajero = choice([1,0.9,0.8,0.7,0.6])
        
        lista_cajeros.append(entidades.Cajero(env, velocidad_cajero))
    
    return lista_cajeros

clientes = generar_clientes(100, 0.03)
cajeros = generar_cajeros(5, 0.5)

