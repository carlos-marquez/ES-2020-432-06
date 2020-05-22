import requests

class Cars:

    def __init__(self, cod_car, lugar_recogida, dias_reserva):
        self.cod_car = cod_car
        self.lugar_recogida = lugar_recogida
        self.dias_reserva = dias_reserva
        pass

    @staticmethod
    def download_seat_leon_specifications():
        r = requests.get('http://localhost/dummy_url')
        if r.status_code == 200:
            return r.json()
        return None