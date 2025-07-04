#################
###  OBJETOS  ###
#################

class Carta :
    """
    Clase Carta; representa un carta del mazo. Esta clase está pensada para ser usada dentro de la clase Mazo; sin embargo, se pueden generar cartas individuales.

    Args:
        palo (str): 'Corazones', 'Diamantes', 'Tréboles', 'Picas'
        valor (str): Valor de la carta ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
    """

    def __init__(self, palo, valor):    # Método;: Inicio de objeto.
        self.palo = palo    # Atributo (str): Palo al que pertenece la carta.
        self.valor = valor  # Atributo (str): Valor nominal de la carta.

class Mazo :
    """
    Clase Mazo, representa un conjunto de cartas.
    """
    def __init__(self): # Método: Inicio del objeto.
        self.mazo = self.generar_cartas()   # Atributo (list): Lista de cartas; se genera automáticamente al iniciar el objeto llamando el método generar_cartas()
        self.tamaño = len(self.mazo)    # Atributo (int): Tamaño del mazo.

    def generar_cartas(self) :
        """
        Método para generar las 52 cartas del mazo. Esta función se auto-llama al crear el objeto mazo.

        Returns:
            mazo (object): Conjunto de 52 cartas.
        """
        palos = ('Corazones', 'Diamantes', 'Tréboles', 'Picas') # Tupla de palos
        valores = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')    # Tupla de valores

        mazo = []   # Lista que almacena las cartas generadas.
        for palo in palos :
            for valor in valores :
                mazo.append(Carta(palo,valor))  # Crea Carta y la agrega en la lista de Cartas (mazo).
    
        return mazo

    def revolver(self) :
        """
        Método para revolver las 52 cartas del mazo.
        """
        import random   # Importa el módulo random usado para revolver las cartas.
        random.shuffle(self.mazo)   # Revuelve los elementos en la lista mazo.

    def repartir(self, jugadores: list, cartas_por_mano: int) :
        """
        Método para repartir las cartas entre los jugadores seleccionados. El método interactúa directamente con la clase Jugador.

        Args:
            jugadores (list): Lista de jugadores.
            cartas_por_mano (int): Cantidad de cartas a repartir a cada jugador.
        """
        num_jugadores = len(jugadores)  # Cuenta el número de Jugadores en la lista de jugadores.

        manos = []  # Lista de manos
        for i in range(0,num_jugadores) :   # Este bucle for reparte las cartas entre cada Jugador i.
            mano = []
            for j in range(0,cartas_por_mano) :     # Este bucle for crea la mano para cada Jugador.
                mano.append(self.mazo[i*cartas_por_mano+j])
            manos.append(mano)    

        for i in range(0,num_jugadores) :   # Este bucle for asigna la mano correspondiente a cada Jugador i.
            jugadores[i].número = i+1
            jugadores[i].mano = manos[i]

class Jugador :
    """
    Clase Jugador; representa un jugador que puede participar en el juego.

    Args:
        nombre (str): Nombre del jugador.
    """
    def __init__(self, nombre):
        self.nombre = nombre
        self.número = 0
        self.mano = []

    def mostrar_mano(self) :
        """
        Método que muestra los atributos "palo" y "valor" de cada objeto carta en la mano del jugador.

        Returns:
            mano (list) : Lista de cartas expresada como f"{valor} de {palo}".
        """
        mano = []
        for carta in self.mano :
            mano.append(f"{carta.valor} de {carta.palo}")
        return mano


###################
###  FUNCIONES  ###
###################

def simular_póquer(mazo: object, jugadores: list, iteraciones: int, mano_a_buscar: str, regenerar_mazo=False) -> dict :
    """
    Función que permite repetir n veces la repartición y búsqueda de un tipo de mano específica de póquer.

    Args:
        mazo (object): Mazo.
        jugadores (list): Lista de jugadores a participar en el juego.
        iteraciones (int): Cantidad de veces a repetir la simulación.
        mano_a_buscar (str): Opciones "Flor Imperial" y "Mano de muerto"
        regenerar_mazo (bool): Opciones True y False. Por defecto False. Para cada jugada crea un nuevo mazo ordenado en lugar de revolver el ya existente.

    Returns:
        Dictionary: Diccionario que contiene la cantidad total de juegos simulados ('Total jugado'), el total de partidas ('Jugadas encontradas') que cumplen con el criterio de búsqueda (flores imperiales o manos de muerto) y la probabilidad de que ocurra el tipo de partida buscada ('Probabilidad').
    """
    
    ### Funciones dentro de la función ###

    def buscar_flores_imperiales(jugador: object) -> bool :
        """
        Función que permite buscar flores imperiales dentro de la mano del jugador.

        Args:
            jugador (object): Jugador.
        """
        valores_imperiales = ('10', 'J', 'Q', 'K', 'A')
    
        palos = [carta.palo for carta in jugador.mano]  # Crea una lista de los palos de las cartas de cada jugador.
        valores = [carta.valor for carta in jugador.mano]   # Crea una lista de los valores de las cartas de cada jugador.

        if len(set(palos)) == 1 :   # Verifica que haya solo palos de un solo tipo en la lista de palos.
            indicador = 0
            for valor in valores :  # Si es así, este bucle for verifica que cada carta tenga un valor imperial.
                if valor in valores_imperiales :
                    indicador += 1  # Si una carta es un valor imperial, suma 1 a un contador.
            return indicador == 5   # Si la variable del contador es igual a 5, entonces retorna True, de lo contrario False.
        else :
            return False

    def buscar_mano_muerto(jugador: object) -> bool:    # Lo mismo que las flores imperiales, pero la mano del muerto.
        """
        Función que permite buscar la mano del muerto dentro de la mano de un jugador.

        Args:
            jugador (object): Jugador.
        """
        valor_muerto = ('8','A')
        palo_muerto = ('Tréboles', 'Picas')

        contador = 0
        for carta in jugador.mano :
            if carta.valor in valor_muerto and carta.palo in palo_muerto :
                contador += 1
        
        return contador == 4
    

    ### Parte de la función que simula los juegos ###

    if len(jugadores) != len(set(jugadores)) :  # Este código verifica que no se agregue un mismo Jugador a la lista.
        raise ValueError("Hay jugadores repetidos en la lista.")
    if len(jugadores) > 52//5 : # Verifica que no se añadan más jugadores de los que se permitan, tomando en cuenta que una mano de póquer es de 5 cartas.
        raise ValueError(f"La cantidad máxima de jugadores es {52//5}.")

    match mano_a_buscar.lower() :   # Este código verifica el tipo de jugada que el usuario quiere simular. Convierte todo el texto en minúsculas para evitar que el código se rompa en caso de que el jugador no siga un patrón estándar.
        case "flor imperial" :
            juego = buscar_flores_imperiales
        case "mano de muerto" :
            juego = buscar_mano_muerto

    jugadas_totales = 0 # Contador del total de jugadas jugadas.
    jugadas_clave = 0   # Contador de partidas en las que hubo una flor imperial.

    for i in range(0,iteraciones) : # Este bucle for permite que el juego se repita (simule) n veces.
        mazo.revolver() # Revuelve las cartas del mazo.
        mazo.repartir(jugadores, 5) # Reparte las cartas entre los jugadores.

        for jugador in set(jugadores) : 
            if juego(jugador) : # Busca el tipo de mano definida por el usuario y solamente imprime la mano si es una flor imperial o una mano de muerto.
                jugadas_clave += 1
                print(f"(Juego# {jugadas_totales+1}) {jugador.nombre}: {jugador.mostrar_mano()}")
    
        jugadas_totales += 1    # Suma el juego en el contador.

        if regenerar_mazo : # Si se escogió regenerar mazo, se genera uno nuevo.
            mazo.generar_cartas()

    return {    # Retorna la información del juego.
        "Total jugado" :  jugadas_totales,
        "Jugadas encontradas" : jugadas_clave,
        "Probabilidad": f"{jugadas_clave / jugadas_totales * 100} %"
    }



#############################
###  CREACIÓN DE OBJETOS  ###
#############################

Juan = Jugador("Juan")
Pedro = Jugador("Pedro")
Pablo = Jugador("Pablo")
Paco = Jugador("Paco")

mazo = Mazo()


###################
###  EjECUCIÓN  ###
###################
# Parámetros: 4 jugadores; 1 millón de partidas; buscar Flor Imperial.

simulación = simular_póquer(mazo, [Juan, Pedro, Pablo, Paco], 1000000, "Flor imperial") # Ejecuta el juego y guarda la información en una variable.
print() # Línea en blanco por cuestión de estilo.
print(simulación)  # Imprime los resultados de la simulación.