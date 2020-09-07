from PressureLoss.LinePressureDrop import LinePressureDrop
from HydraulicLibrary.functions.calculateVelocity import calculateVelocity


class Hose:

    def __init__(self, name, viscosity, diameter, flow, length):

        self.name = name
        self.viscosity = viscosity
        self.diameter = diameter
        self.flow = flow
        self.length = length

    def hoseName(self):
        return self.name

    def pressureDrop(self):
        linePressureDrop = LinePressureDrop(self.viscosity, self.diameter, self.flow, self.length).calculateLinePressureDrop()
        return linePressureDrop

    def flowVelocity(self):
        velocity = calculateVelocity(self.flow, self.diameter)
        return  velocity


    def printParameters(self):
        print "Name = ", self.name, ""
        print "dp = ", self.pressureDrop(), "[bar] "
        print "v = ", self.flowVelocity(), " [m/s] \n"



