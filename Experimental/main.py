from random import randrange
import entities
import datetime as dt

client_qty = 100

client_list = []

for i in range(0,client_qty) :
    client = entities.Client()
    client.cart_size = randrange(1,50)
    client_list.append(client)

cashier = entities.Cashier()

start_date = dt.datetime.now()

while len(client_list) > 0 :
    cashier.call_client(client_list)
    cashier.scan()

end_date = dt.datetime.now()

print(f"El proceso tomó {(end_date-start_date).total_seconds()} segundos.")