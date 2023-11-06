from Car import Car

class GasolineCar(Car.Car):
    def __init__(self, makeAndModel = "none assigned", numberOfDoors = 4, maximumNumberOfPassengers = 5, gasTankSize = -1):
        super().__init__(makeAndModel, numberOfDoors, maximumNumberOfPassengers)
        self.gasTankSize = gasTankSize

    def getGasTankSize(self):
        return(self.gasTankSize)

    def setGasTankSize(self, gasTankSize):
        self.gasTankSize = gasTankSize
    def __str__(self):
        return(super().__str__() + "\n gas tank size: " + str(self.gasTankSize))
if __name__ == "__main__":
    GasCar1 = GasolineCar()
    print(GasCar1.getGasTankSize())