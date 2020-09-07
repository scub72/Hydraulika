from HydraulicLibrary.PressureDropCoefficient import PressureDropCoefficient
import math
from HydraulicLibrary.OilParameters import *
from HydraulicLibrary.functions.calculateVelocity import calculateVelocity


class LinePressureDrop:

    def __init__(self, viscosity, diameter, flow, length):

        self.viscosity = viscosity
        self.diameter = diameter
        self.flow = flow
        self.length = length
        self.velocity = calculateVelocity(self.flow, self.diameter)

    def calculateLinePressureDrop(self):

        op = OilParameters()
        pdc = PressureDropCoefficient(self.viscosity, self.diameter, self.flow).calculatePressureDropCoefficient()
        pressureDrop = pow(10.0, 3)*pdc*self.length*op.density*pow(self.velocity, 2)/self.diameter/2/pow(10.0, 5)
        return pressureDrop


