class Car:
    def __init__(self, makeAndModel:str = "none assigned", numberOfDoors:int = 4, maximumNumberOfPassengers:int = 5):
        self.makeAndModel = makeAndModel
        self.numberOfDoors = numberOfDoors
        self.maximumNumberOfPassengers = maximumNumberOfPassengers

    def setMakeAndModel(self, make_model):
        self.makeAndModel = make_model

    def getMakeAndModel(self):
        return (self.makeAndModel)
    
    def get_maximumNumberOfPassengers(self):
        return (self.maximumNumberOfPassengers)
    
    def __str__(self):
        stringToReturn = " make model: " + self.makeAndModel + "\n number of doors: " + str(self.numberOfDoors) + "\n max passengers: " + str(self.maximumNumberOfPassengers)
