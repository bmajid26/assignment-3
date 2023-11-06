from Car import Car
from ElectricCar import ElectricCar
from GasolineCar import GasolineCar
from LinkedList import LinkedList


testList = LinkedList()

car1 = ElectricCar("test electric car", 6, 1)
car2 = Car("test car", 7, 1)
car3 = Car("testCar2")
car4 = GasolineCar("test gas car")
testList.add(car1)
testList.add(car2)
testList.add(car3)

testList.delete(0) #deleting first element
testList.delete(1) #deleting the middle element
testList.delete(2) #deleting the last element

testList.insert(1, car4) #head insert
testList.insert(0, car4) #insert at middle of list
testList.insert(3, car4) #tail insert
print()

