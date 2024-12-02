from typing import Dict
from classes.measurement import Measurement
import math

class Model:
    def __init__(self, measurements: Dict[str, Measurement]):
        self.measurements = measurements

    def __str__(self):
        result = ''
        for k in self.measurements.keys():
            result += k + ': ' + self.measurements[k].__str__() + '\n'
        return result
    
    def get_measurements(self):
        return self.measurements
    
    def set_measurements(self, measurements):
        self.measurements = measurements

    def make_recipe(self, calibration):
        pass

    def lacking_measurements(self):
        for m in self.measurements.keys():
            none_measurement = (self.measurements[m].get_value() is None)
            zero_measurement = (self.measurements[m].get_value() == 0.0)
            if none_measurement or zero_measurement:
                return True
        return False
    
class Quadrado(Model):
    def __init__(self):
        measurements = {
            'largura': Measurement(),
            'altura': Measurement()
        }
        Model.__init__(
            self, measurements
        )
    
    def __str__(self):
        return 'Quadrado \n' + super().__str__()
    
    def make_recipe(self, calibration):
        columns = math.ceil(
            self.measurements['largura'].get_value() / calibration['column_width']
        )
        rows = math.ceil(
            self.measurements['altura'].get_value() / calibration['row_height']
        )

        final_width = columns * calibration['column_width']
        final_height = rows * calibration['row_height']
        total_stiches = columns * rows

        recipe = f'''
        Inicie com uma correntinha de tamanho {columns}.
        Depois, faça {rows} fileiras de pontos.
        Sua peça terá {total_stiches} pontos no total, e um tamanho de {final_width} x {final_height}.
        '''

        return recipe, total_stiches
