from random import randrange
from time import sleep
import entidades_old as entidades
import datetime as dt

customer_qty = 100
cashier_qty = 5

customer_list = []
cashier_list = []

for i in range(customer_qty) :
    customer = entidades.Cliente()
    customer.id_cliente = i+1
    customer.tamaño_carrito = randrange(1,50)
    customer_list.append(customer)

for i in range(cashier_qty) :
    cashier = entidades.Cajero()
    cashier.id_cajero = i+1
    cashier_list.append(cashier)

start_date = dt.datetime.now()

while len(customer_list) > 0 :
    
    sigma_scanning_queue = 0
    for cashier in cashier_list :
        cashier.artículos_escaneados = 0
        cashier.llamar_cliente(customer_list)
        print(f"Cliente {cashier.cliente_actual.id_cliente} asignado a cajero {cashier.id_cajero}: {cashier.cliente_actual.tamaño_carrito} por escanear.")
        sigma_scanning_queue += cashier.cliente_actual.tamaño_carrito
    
    while sigma_scanning_queue > 0 :
        cycle_scanning_queue = 0
        for cashier in cashier_list :
            if cashier.cliente_actual.tamaño_carrito > 0 :
                cashier.escanear_uno()
                #print(f"{cashier.scanned_items} artículos escaneados.")
                cycle_scanning_queue += cashier.cliente_actual.tamaño_carrito
        sleep(0.1)
        sigma_scanning_queue = cycle_scanning_queue

end_date = dt.datetime.now()

print(f"El proceso tomó {(end_date-start_date).total_seconds()} segundos.")