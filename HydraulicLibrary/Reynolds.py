


#
# Class calculates Reynolds number
#   with given:
#   - viscosity     in [CSt]
#   -diameter       in [mm]
#   -flow           in [l/min]
#
#
from HydraulicLibrary.functions.calculateVelocity import calculateVelocity


class Reynolds:

    def __init__(self, viscosity, diameter, flow):
        self.viscosity = viscosity
        self.diameter = diameter
        self.flow = flow

    def calculateRe(self):
        reynoldsNumber = calculateVelocity(self.flow, self.diameter)*self.diameter*1000.0/self.viscosity
        return reynoldsNumber


