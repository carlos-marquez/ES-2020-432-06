class Flights:

    def init(self):
        self.listado_vuelos = []

    def add_vol(self,cod_vuelo, destino, n_pasajeros):
        aux = Vuelos(cod_vuelo, destino, n_pasajeros)
        self.listado_vuelos.append(aux)