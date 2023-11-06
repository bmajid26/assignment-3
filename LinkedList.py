from Node import Node

# import Car
# import ElectricCar
# import GasolineCar
# import Node
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, item:object):
        newNode = Node(item)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            current_last = self.tail
            current_last.setNext(newNode)
            newNode.setPrevious(current_last)
            self.tail = newNode
        self.size = self.size + 1

    def insert(self, index, item):
        newNode = Node(item)
        current = self.head
        if(self.size > 0 and index <= self.size):
            if(index == 0):
                self.head = newNode
                current.setPrevious(newNode)
                newNode.setNext(current)
            elif(index == self.size):
                current = self.tail
                self.tail = newNode
                current.setNext(newNode)
                newNode.setPrevious(current)
            else:
                i = 0
                while (i < index):
                    current = current.getNext()
                    i = i + 1
                current.getPrevious().setNext(newNode)
                newNode.setPrevious(current.getPrevious())
                current.setPrevious(newNode)
                newNode.setNext(current)
            self.size = self.size + 1
    def delete(self, i):
        if self.size != 0:
            if i == 0:
                temp_head = self.head.getNext()
                self.head = temp_head
                self.size = self.size - 1
                if (self.size != 0):
                    temp_head.setPrevious(None)
                else:
                    self.head = None
                    self.tail = None

            elif i == self.size - 1:
                j = 0
                temp2 = self.head
                while j != i:
                    temp2 = temp2.getNext()
                    j = j + 1
                prev = temp2.getPrevious()
                prev.setNext(None)
                self.tail = prev
                self.size = self.size - 1

            else:
                j = 0
                temp = self.head
                while (j != i):
                    temp = temp.getNext()
                    j = j + 1
                prev = temp.getPrevious()
                next = temp.getNext()
                prev.setNext(next)
                next.setPrevious(prev)
                self.size = self.size - 1

    def length(self):
        return(self.size)
    def __getitem__(self, index):
        current = self.head
        x = 0
        while (x < index):
            current = current.getNext()
            x = x + 1
        return(current.getData())

    def __str__(self):
        stringToReturn = "list size: " + str(self.size)
        current = self.head
        while (current is not None):
            stringToReturn = stringToReturn + "\n\n" + str(current)
            current = current.getNext()
        return(stringToReturn)