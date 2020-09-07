import math
from HydraulicLibrary.Reynolds import Reynolds

#Class calculates the pressure drop coefficient - lambda based on the Reynolds number
#
#

class PressureDropCoefficient:

    def __init__(self, viscosity, diameter, flow):

        self.viscosity = viscosity
        self.diameter = diameter
        self.flow = flow

    def calculatePressureDropCoefficient(self):

       reynoldsNumber = Reynolds(self.viscosity, self.diameter, self.flow).calculateRe()
       pressureDropCoefficient = 64.0/reynoldsNumber
       return pressureDropCoefficient






