from Car import Car

class ElectricCar(Car.Car):
    def __init__(self, makeAndModel:str = "none assigned", numberOfDoors = 4, maximumNumberOfPassengers = 5, batterySize = -1):
        super().__init__(makeAndModel, numberOfDoors, maximumNumberOfPassengers)
        self.batterySize = batterySize

    def getBatterySize(self):
        return(self.batterySize)

    def setBatterySize(self, battery_size):
        self.batterySize = battery_size
    def __str__(self):
        return(super().__str__() + "\n battery size: " + str(self.batterySize))
if __name__ == "__main__":
    electricCar1 = ElectricCar()
    print(electricCar1.getBatterySize())