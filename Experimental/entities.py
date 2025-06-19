class Cashier() :
    def __init__(self):
        self.current_client = None
        self.scan_speed = 0.1 # In seconds

    def call_client(self, client_list: list) :
        self.current_client = client_list[0]
        del client_list[0]
    
    def scan(self) :
        from time import sleep
        current_cart_size = self.current_client.cart_size
        while self.current_client.cart_size > 0 :
            self.current_client.cart_size -= 1
            sleep(self.scan_speed)
        
        print(f"{current_cart_size} escaneados.")

class Client() :
    def __init__(self):
        self.cart_size = 0