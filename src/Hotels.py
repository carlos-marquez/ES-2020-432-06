import os
import os.path

class Hotels:

    def __init__(self, cod_hotel = '123', nombre_hotel = 'Vela', num_huespedes = '3', num_hab = '311', reserva = '2611'):
        self.cod_hotel = cod_hotel
        self.nombre_hotel = nombre_hotel
        self.num_huespedes = num_huespedes
        self.num_hab = num_hab
        self.reserva = reserva
        pass

    def rm(self, filename):
        """Dummy function to remove a file.

        Args:
            filename (str): path to the file.
        """    
        if os.path.isfile(filename):
            os.remove(filename)
    
    @staticmethod
    def get_always_true():
        """Dummy function to return always true

        Returns:
            [bool]: Return true.
        """        
        return True

class Alojamiento:
    def init(self):
        self.lista_alojamiento = []

    def add_alojamiento(self, cod_hotel, nombre_hotel, num_huespedes, num_hab, reserva):
        aux = Hotels(cod_hotel, nombre_hotel, num_huespedes, num_hab, reserva)
        self.lista_alojamiento.append(aux)