import requests

class Cars:

    def __init__(self, cod_car = '123', marca = 'BMW', lugar_recogida = 'BCN', dias_reserva = '4'):
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
 
class Vehiculo:
    def init(self):
        self.listado_coches = []

    def add_coche(self, cod_car, marca, lugar_recogida, dias_reserva):
        aux = Cars(cod_car, marca, lugar_recogida, dias_reserva)
        self.listado_coches.append(aux)
