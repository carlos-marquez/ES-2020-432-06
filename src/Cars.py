import requests
from src.Rentalcars import Rentalcars
from src.User import User
class Cars:

    def __init__(self, cod_car, marca, lugar_recogida, dias_reserva):
        self.cod_car = cod_car
        self.marca = marca
        self.lugar_recogida = lugar_recogida
        self.dias_reserva = dias_reserva
        pass

    @staticmethod
    def download_seat_leon_specifications():
        r = requests.get('http://localhost/dummy_url')
        if r.status_code == 200:
            return r.json()
        return None
    def comprueba(self,cod_car,marca,lugar_recogida,dias_reserva):
        val_boleano = 1
        if cod_car == '':
            val_boleano = 0
        if marca == '':
            val_boleano == 0
        if lugar_recogida == '':
            val_boleano == 0
        if dias_reserva == '' and dias_reserva <= 0:
            val_boleano == 0
        return val_boleano
class Vehiculo:
    def init(self):
        self.listado_coches = []

    def add_coche(self, cod_car, marca, lugar_recogida, dias_reserva):
        aux = Cars(cod_car, marca, lugar_recogida, dias_reserva)
        self.listado_coches.append(aux)

    
        