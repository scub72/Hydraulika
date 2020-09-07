import matplotlib.pyplot as plt
import numpy as np

class Cooler:

    def __init__(self):

        #the variables indicates the coller parameters read from the cooler graph
        self.pressureDrop       = []
        self.flowAtPressureDrop = []
        self.coolingCapacity    = []
        self.ambientAndOilTemperatureDifference = [10., 20., 30., 40.]
        self.name = ".............."



    # reserve() calculates the reserve which is the result of substraction of check valve setting and cooler pressure drop
    def reserve(self, checkValveSetting):

        reserve = []
        for i in range(0, len(self.pressureDrop), 1):
            reserve.append(checkValveSetting - self.pressureDrop[i])

        return reserve

    # creates plot of the transfered power in flow function according to the difference between the enviorment and oil temperature
    def transferdPowerPlot(self):

        flow = self.flowAtPressureDrop
        transferedPowerAtTemp = self.transferedPowerAndFlowCharacteristics()
        dT10 = plt.plot(flow, transferedPowerAtTemp[0], 'r--',
                        label='Moc odprowadzona przy roznicy czynnik - srodowisko 10 stopni C')
        dT20 = plt.plot(flow, transferedPowerAtTemp[1], 'r-',
                        label='Moc odprowadzona przy roznicy czynnik - srodowisko 20 stopni C')
        dT30 = plt.plot(flow, transferedPowerAtTemp[2], 'b--',
                        label='Moc odprowadzona przy roznicy czynnik - srodowisko 30 stopni C')
        dT40 = plt.plot(flow, transferedPowerAtTemp[3], 'b-',
                        label='Moc odprowadzona przy roznicy czynnik - srodowisko 40 stopni C')

        plt.yticks(np.arange(0, max(transferedPowerAtTemp[3]) + 1, 0.5))
        plt.xticks(np.arange(0, max(flow) + 20, 10))
        plt.title("Wykres zaleznosci odprowadzonej mocy przez chlodnice " + self.getName() + " w zaleznosci od natezenia przeplywu dla poszczegolnych roznic temperatury otoczenia i temperatury oleju \n")
        plt.xlabel("Flow [l/min]")
        plt.ylabel("Transfered Power [kW]")
        plt.legend()
        plt.grid()
        plt.figure()

    # prepares array of the transfered power to create the  transferedPowerPlot figure
    def transferedPowerAndFlowCharacteristics(self):

        transferedPowerAtTemp=[]

        for i in range(0, len(self.ambientAndOilTemperatureDifference),1):

            transferedPower = []
            for j in range(0,len(self.coolingCapacity),1):

                tp=self.coolingCapacity[j]*self.ambientAndOilTemperatureDifference[i]
                transferedPower.append(tp)

            transferedPowerAtTemp.append(transferedPower)

        return transferedPowerAtTemp


    def setName(self, name):
        self.name=name

    def getCoolerPressureDrop(self):
        return self.pressureDrop

    def getCoolerFlowAtPressureDrop(self):
        return self.flowAtPressureDrop

    def getCoolingCapacity(self):
        return self.coolingCapacity

    def getAmbientAndOilTemperatureDifference(self):
        return self.ambientAndOilTemperatureDifference

    def getName(self):
        return self.name

    def setCoolerPressureDrop(self, pressureDrop):
        self.pressureDrop = pressureDrop

    def setCoolerFlowAtPressureDrop(self, flowAtPressureDrop):
        self.flowAtPressureDrop = flowAtPressureDrop

    def setCoolingCapacity(self, coolingCapacity):
        self.coolingCapacity=coolingCapacity

    def setAmbientAndOilTemperatureDifference(self, ambientAndOilTemperatureDifference):
        self.ambientAndOilTemperatureDifference=ambientAndOilTemperatureDifference

