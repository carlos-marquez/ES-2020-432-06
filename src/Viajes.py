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

    def funcion1(self, n_pasajeros, lista_pasajeros):
       final = False
       if n_pasajeros == len(lista_pasajeros):
           final == True
       return final
    pass
    
    def calcular_precio(self):
        return self.precio * self.n_pasajeros * len(self.lista_destinos)
    pass


    def eliminar_destino(self, destino):
       if destino in self.lista_destinos:
            index = self.lista_destinos.index(destino)
            new_d = [
                    self.lista_destinos[i] 
                    for i in range(len(self.lista_destinos))
                    if i != index
                    ]
                    

            new_v = [                                                                                                                                                                                                                                                                                                                               
                    self.vuelos[i] 
                    for i in range(len(self.vuelos))
                    if i != index
                    ]                                                                                                       

            self.lista_destinos = new_d
            self.vuelos = new_v

    def payment(self, tipo_tarjeta, titular_tarjeta, cod_seg_tarjeta):
        precio_final = self.calcular_precio()
        x = Bank()
        self.payment_data = PaymentData(tipo_tarjeta, titular_tarjeta, cod_seg_tarjeta, precio_final)
        return x.do_payment(self.user, self.payment_data)


    def anadir_reserva(self):
        aux = Skyscanner()
        return aux.confirm_reserve(self.user)

    def comprueba_datos(self, nombre, DNI, Dir_Postal, telf, mail):
        if (nombre.isdigit()):
            correcto=False
        elif (not DNI.isalpha()):
            correcto=False
        elif (Dir_Postal.isalpha()):
            correcto=False
        elif (telf.isalpha()):
            correcto=False
        elif (mail.isalnum()):
            correcto=False
        return correcto
        
    def datos_completos(self, nombre, DNI, Dir_Postal, telf, mail):
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
        