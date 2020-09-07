#
#   Pressure drop calculation in the cooler circuit
#   with the given hosses and connectors
#   generates plot which shows pressure drop and flow dependency p(Q) in a different viscosity
#

import matplotlib.pyplot as plt
import numpy as np
from PressureLoss.StraightConnectorPressureDrop import StraightConnectorPressureDrop
from PressureLoss.ElbowConnectorPressureDrop import ElbowConnectorPressureDrop
from HydraulicComponents.Hose import Hose
from HydraulicComponents.Cooler import Cooler
import MathFunctions.Matrix as mtx



#   temp.       20  30  40  50  60  70
#   viscosity   120 75  46  29  21  15,5
#   flow   0-350

# Viscosity matrix Shell Tellus HV46
viscosity   = [120, 75, 46, 29, 21, 15.5]
OilTemp     = [20,  30, 40, 50, 60, 70 ]

#
# Cooler characteristic -  pressure drop dependency
# dp                [ 0.01, 0.05,   0.1,    0.16,   0.22,   0.28,   0.36,   0.44,   0.55,   0.65,   0.74,   0.84]
#  Q                [ 10,   20,     30,     40,     50,     60,     70,     80,     90,     100,    110,    120]
# Cooling capacity  [ 0.15, 0.25,   0.29,   0.31,   0.33,   0.34,   0.35,   0.355,  0.36,   0.37,   0.375,  0.378]
#
# Env temp - oil temp = dT
# dT = [10, 20, 30, 40]

# Defining the cooler parameters Parker LDC 016
pdCooler =          [ 0.01,  0.05,  0.1,    0.16,   0.22,   0.28,   0.36,   0.44,  0.55,  0.65,    0.74,    0.84]
pdCoolerFlow =      [ 10,    20,    30,     40,     50,     60,     70,     80,   90,    100,     110,    120]
coolingCapacity =   [ 0.35, 0.42,   0.46,   0.5,   0.52,   0.54,   0.55,   0.558,  0.568,   0.576,   0.58,  0.582]
#dT =                [10, 20, 30, 40]

oilCooler=Cooler()
oilCooler.setName("Parker LDC 023")
oilCooler.setCoolerPressureDrop(pdCooler)
oilCooler.setCoolerFlowAtPressureDrop(pdCoolerFlow)
oilCooler.setCoolingCapacity(coolingCapacity)
reserve1 = oilCooler.reserve(1)
reserve1_4 = oilCooler.reserve(1.4)

#
# Pressure drop and flow list to generate the characteristics
#
#   pressure drop calculation for the pipes and Hoses in the cooler circuit
#
pd = []
flow1 = []

for i in range(0, len(viscosity)):

    flowMatrix = []
    pdFromFlow = []

    for flow in range(1, 150+1, 1):

        hose1 = Hose("P51P51/111/25x3700",viscosity[i], 25.0, flow, 3.7)
        elbows1 = ElbowConnectorPressureDrop(flow,3.0,25.0).calculateElbowPressureDrop()
        straights1 = StraightConnectorPressureDrop(flow,4.0,25.0).calculateStraightConnectorPressureDrop()
        pd1 = hose1.pressureDrop()+elbows1+straights1

        hose2 = Hose("P51P52/111/25x3000",viscosity[i], 25.0, flow, 3.0)
        elbows2 = ElbowConnectorPressureDrop(flow,1.0,18.0).calculateElbowPressureDrop()
        straights2 = StraightConnectorPressureDrop(flow,1.0,18.0).calculateStraightConnectorPressureDrop()
        pd2 = hose2.pressureDrop()+elbows2+straights2

        hose3 = Hose("P51P52/111/25x6500",viscosity[i], 25.0, flow, 6.5)
        elbows3 = ElbowConnectorPressureDrop(flow,1.0,25.0).calculateElbowPressureDrop()
        straights3 = StraightConnectorPressureDrop(flow,1.0,25.0).calculateStraightConnectorPressureDrop()
        pd3 = hose3.pressureDrop()+elbows3+straights3


        totalPressureDrop = pd1+pd2+pd3
        flowMatrix.append(flow)
        pdFromFlow.append(totalPressureDrop)




    pd.append(pdFromFlow)
    flow1.append(flowMatrix)
#====================================================================================================================#
#============================================ P L O T S =============================================================#
#============================================           =============================================================#

#
#       pressure drop in flow characteristics according to the viscosity
#
visc120 = plt.plot(flow1[0], pd[0], 'r--', label='Lepkosc 120 cSt (20 stopni C)')
visc75 = plt.plot(flow1[1], pd[1], 'r-', label='Lepkosc 75 cSt (30 stopni C)')
visc46 = plt.plot(flow1[2], pd[2], 'b--', label='Lepkosc 46 cSt (40 stopni C)')
visc29 = plt.plot(flow1[3], pd[3], 'b-', label='Lepkosc 29 cSt (50 stopni C)')
visc21 = plt.plot(flow1[4], pd[4], 'g--', label='Lepkosc 21 cSt (60 stopni C)')
visc15 = plt.plot(flow1[5], pd[5], 'g-', label='Lepkosc 15.5 cSt (70 stopni C)')
cooler = plt.plot(oilCooler.getCoolerFlowAtPressureDrop(), reserve1, 'y-', label="Zapas dla nastawy zaworu 1 bar")
cooler2 = plt.plot(oilCooler.getCoolerFlowAtPressureDrop(), reserve1_4, 'y-', label="Zapas dla nastawy zaworu 1.4 bar")

plt.title("Wykres zaleznosci spadku cisnienia przewodow obwodu chlodnicy " + oilCooler.getName() + " dla roznych temperatur oleju - przeciecie zoltych linii na wykresie\n"
          " oznacza otwarcie zaworu zwrotnego odpowiednio przy 1 i przy 1.4 bar \n")
plt.yticks(np.arange(0, max(pd[0])+1, 0.1))
plt.xticks(np.arange(0, max(flow1[0])+20, 10))
plt.xlabel("Flow [l/min]")
plt.ylabel("Pressure drop [bar]")
plt.legend()
plt.grid()
plt.figure()

#
#   transfered power with flow characteristics
#   according to the difference between the enviorment and oil temperarature
#

oilCooler.transferdPowerPlot()

#
#   total pressure drop characteristics for the 30cSt characteristics
#

q = flow1[3]
p=pd[3]
qbuff=[]
pbuff=[]

for i in range(0, len(flow1[3]), 1):

    for j in range(0, len(pdCoolerFlow),1):

        if q[i] == pdCoolerFlow[j]:
            pbuff.append(p[i])
            qbuff.append(q[i])

pdSuma = mtx.sumList(pbuff,pdCooler)
visc30=plt.plot(qbuff, pdSuma, 'g-', label='Zaleznosc sumarycznego spadku cisnienia dla lepkosci 30 cSt(50 stopni C)')
visc30pkt=plt.plot(qbuff, pdSuma, 'ro')
plt.yticks(np.arange(0, max(pdSuma)+0.1, 0.1))
plt.xticks(np.arange(0, max(qbuff)+10, 5))
plt.xlabel("Flow [l/min]")
plt.ylabel("Pressure drop [bar]")
plt.legend()
plt.grid()
plt.show()





