from HydraulicLibrary.functions import calculateVelocity
from HydraulicLibrary.OilParameters import OilParameters
from HydraulicLibrary.functions.calculateVelocity import calculateVelocity

class ElbowConnectorPressureDrop:

    def __init__(self, flow, count, diameter):

        op = OilParameters()
        self.flow = flow
        self.count = count
        self.diameter = diameter
        self.velocity = calculateVelocity(self.flow, self.diameter)
        self.elbowPressureDropCoefficient = 0.15
        self.density = op.density

    def calculateElbowPressureDrop(self):

        elbowConnectorPressureDrop = self.count*self.elbowPressureDropCoefficient*self.density*pow(self.velocity, 2)/2/pow(10.0, 5)
        return elbowConnectorPressureDrop
