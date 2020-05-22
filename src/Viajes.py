from src.User import User
from src.PaymentData import PaymentData
from src.Skyscanner import Skyscanner
from src.Bank import Bank

class Viajes:

    def __init__(self, user: User = None, lista_pasajeros = ['p1','p2','p3','p4'], vuelos = [], coches = [], hoteles = []):
        self.user = user
        self.payment_data = None
        self.n_pasajeros = len(lista_pasajeros)
        self.lista_pasajeros = lista_pasajeros
        self.lista_destinos = [i.destino for i in vuelos]
        self.precio = 50
        self.vuelos = vuelos
        self.coches = coches
        self.hoteles = hoteles
        pass

    def anadir_reserva(self):
        aux = Skyscanner()
        return aux.confirm_reserve(self.user)

    def comprueba_datos(self, nombre, DNI, Dir_Postal, telf, mail):
        if (nombre==' '):
            correcto=False
        elif (DNI==' '):
            correcto=False
        elif (Dir_Postal==' '):
            correcto=False
        elif (telf==' '):
            correcto=False
        elif (mail==' '):
            correcto=False
        return correcto
        
