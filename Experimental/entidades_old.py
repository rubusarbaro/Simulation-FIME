class Cajero() :
    def __init__(self):
        #self.environment = env
        self.id_cajero = 0
        #self.velocidad_escaneo = velocidad_escaneo # En segundos; 0.1 por defecto.
        self.fila_clientes = []
        self.cliente_actual = None
        self.artículos_escaneados = 0

    def llamar_cliente(self, fila_clientes: list) :
        self.artículos_escaneados = 0
        self.cliente_actual = fila_clientes[0]
        del fila_clientes[0]
    
    def escanear(self) :
        from time import sleep
        tamaño_carrito_actual = self.cliente_actual.tamaño_carrito
        while self.cliente_actual.tamaño_carrito > 0 :
            self.cliente_actual.tamaño_carrito -= 1
            sleep(self.velocidad_escaneo)
        
        print(f"{tamaño_carrito_actual} escaneados.")

    def escanear_uno(self) :
        self.cliente_actual.tamaño_carrito -= 1
        self.artículos_escaneados += 1

class Cliente() :
    def __init__(self):
        #self.environment = env
        self.id_cliente = 0
        #self.tipo_cliente = tipo_cliente  # Tipos: regular y observador
        self.tamaño_carrito = 0
    
    def formarse_fila(self, cajeros_lista: list) :
        from math import inf
        fila = None
        match self.tipo_cliente :
            case "regular" :
                tamaño_fila = inf
                for cajero in cajeros_lista :
                    if len(cajero.fila_clientes) < tamaño_fila :
                        tamaño_fila = len(cajero.fila_clientes)
                        fila = cajero
            case "observador" :
                tamaño_artículos_fila = inf
                for cajero in cajeros_lista :
                    tamaño_carritos = 0
                    for cliente in cajero.fila_clientes :
                        tamaño_carritos += cliente.tamaño_carrito
                    
                    if tamaño_carritos < tamaño_artículos_fila :
                        tamaño_artículos_fila = tamaño_carritos
                        fila = cajero
        fila.fila_clientes.append(self)