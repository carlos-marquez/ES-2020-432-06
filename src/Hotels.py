import os
import os.path

class Hotels:

    def __init__(self, cod_hotel, nombre_hotel, num_huespedes, num_hab, reserva):
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
    def comprueba_hoteles(self,cod_hotel,nombre_hotel,num_huespedes,num_hab,reserva):
        val_boleano = 1
        if cod_hotel == '':
            val_boleano = 0
        if nombre_hotel == '':
            val_boleano = 0
        if num_huespedes == '' and num_huespedes <= 0:
            val_boleano = 0
        if num_hab == '' and num_hab <= 0:
            val_boleano = 0
        if reserva == '' and reserva <= 0:
            val_boleano = 0
        return val_boleano
class Alojamiento:
    def init(self):
        self.lista_alojamiento = []

    def add_alojamiento(self, cod_hotel, nombre_hotel, num_huespedes, num_hab, reserva):
        aux = Hotels(cod_hotel, nombre_hotel, num_huespedes, num_hab, reserva)
        self.lista_alojamiento.append(aux)