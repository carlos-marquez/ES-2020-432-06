from src.User import User
from src.PaymentData import PaymentData
from src.Skyscanner import Skyscanner
from src.Rentalcars import Rentalcars
from src.Booking import Booking
from src.Bank import Bank
from src.Cars import Cars, Vehiculo
from src.Hotels import Hotels, Alojamiento
from src.Flights import Flights, Vuelos

class Viajes:

    def __init__(self, user: User = None, lista_pasajeros = ['p1','p2','p3','p4'], vuelos = [], coches = [], hoteles = []):
        self.user = user
        self.payment_data = None
        self.n_pasajeros = len(lista_pasajeros)
        self.lista_pasajeros = lista_pasajeros
        self.vuelos = vuelos
        self.lista_destinos = [i.destino for i in vuelos]
        self.precio = 50
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
        if self.vuelos != []:
            return self.precio * self.n_pasajeros * len(self.lista_destinos)
        else:
            if self.coches != []:
                return self.precio * self.n_pasajeros * len(self.coches)
            else:
                return self.precio * self.n_pasajeros * len(self.hoteles)
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
    
    def eliminar_coches(self, coches):
       if coches in self.coches:
            index = self.coches.index(coches)
            new_d = [
                    self.coches[i] 
                    for i in range(len(self.coches))
                    if i != index
                    ]                                                                                                    

            self.coches = new_d 
    
    def eliminar_alojamiento(self, hoteles):
        if hoteles in self.hoteles:
                index = self.hoteles.index(hoteles)
                new_d = [
                        self.hoteles[i] 
                        for i in range(len(self.hoteles))
                        if i != index
                        ]                                                                                                    

                self.hoteles = new_d 


    def payment_V1(self, tipo_tarjeta, titular_tarjeta, cod_seg_tarjeta):
        precio_final = self.calcular_precio()
        x = Bank()
        self.payment_data = PaymentData(tipo_tarjeta, titular_tarjeta, cod_seg_tarjeta, precio_final)
        return x.do_payment(self.user, self.payment_data)
    
    def payment_V2(self, payment, e=0):
        if e:
            return False
        
        x = Bank()

        self.payment_data = payment
        
        return x.do_payment(self.user, self.payment_data)

    def payment_V3(self, payment, e=0,reintentos=0, max=0):
        if e:
            return False
        if reintentos:
            return False 
        if max >= 3:
            exit(0)
        
        x = Bank()

        self.payment_data = payment
        
        return x.do_payment(self.user, self.payment_data)


    def anadir_reserva(self, e=0):
        if e:
            return False
        s = Skyscanner()
        return s.confirm_reserve(self.user, self.vuelos) 
        
    def anadir_reserva_1(self, e=0, reintentos=0, max=0):
        if e:
            return False
        if reintentos:
            return False 
        if max >= 3:
            exit(0)

        s = Skyscanner()
        return s.confirm_reserve(self.user, self.vuelos) 
    


    def anadir_coche(self,  e=0):
        if e:
            return False
        s = Rentalcars()
        return s.confirm_reserve(self.user, self.coches)  


    


