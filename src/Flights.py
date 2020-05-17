class Vuelos:

    def __init__(self, cod_vuelo=1531666, destino='BCN', n_pasajeros=1):
        self.cod_vuelo = cod_vuelo
        self.destino = destino
        self.n_pasajeros = n_pasajeros
        pass

class Flights:
    def init(self):
        self.listado_vuelos = []

    def add_vol(self,cod_vuelo, destino, n_pasajeros):
        aux = Vuelos(cod_vuelo, destino, n_pasajeros)
        self.listado_vuelos.append(aux)