<<<<<<< HEAD
from src.User import User
from src.PaymentData import PaymentData
from src.Skyscanner import Skyscanner
from src.Bank import Bank
from src.Cars import Cars, Vehiculo
from src.Hotels import Hotels, Alojamiento
from src.Rentalcars import Rentalcars
from src.Booking import Booking
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
        #self.listado_coches = [i.cod_car for i in coches]
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


    def payment(self, tipo_tarjeta, titular_tarjeta, cod_seg_tarjeta):
        precio_final = self.calcular_precio()
        x = Bank()
        self.payment_data = PaymentData(tipo_tarjeta, titular_tarjeta, cod_seg_tarjeta, precio_final)
        return x.do_payment(self.user, self.payment_data)

    def anadir_reserva(self):
        aux = Skyscanner()
        return aux.confirm_reserve(self.user)                                                                                       

    def confirmacion_coches(self,n_pasajeros,cod_car,marca,lugar_recogida,dias_reserva):
        coche = Rentalcars()
        self.aux = Cars(cod_car,marca,lugar_recogida,dias_reserva)
        comp = aux.comprueba(self.aux,cod_car,marca,lugar_recogida,dias_reserva) 
        if comp == 1 and n_pasajeros <= 4:
            return coche.confirm_reserve(self.user)
        else: 
            return -1
    
    def confirmacion_alojamiento(self,cod_hotel,nombre_hotel,num_huespedes,num_hab,reserva):
        hotel = Booking()
        self.aux = Hotels(cod_hotel,nombre_hotel,num_huespedes,num_hab,reserva)
        comp = aux.comprueba_hoteles(self.aux,cod_hotel,nombre_hotel,num_huespedes,num_hab,reserva)
        cap = num_huespedes/num_hab
        if comp == 1 and cap <= 3:
            return hotel.confirm_reserve(self.user)
        else:
            return -1
=======
class Viajes:

     def __init__(self, n_pasajeros:int, lista_pasajeros:list, num_destinos:list):
        self.n_pasajeros = n_pasajeros
        self.lista_pasajeros = lista_pasajeros
        self.num_destinos = num_destinos
        #self.vuelos = vuelos
        #self.coches = coches
        #self.hoteles = hoteles
        pass
>>>>>>> 3969d18b9f8d326e4ed3144530b5e6ad741dad47
