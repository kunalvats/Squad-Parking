class Slot:

    __isCarParked = False
    __slotId = 0

    def __init__(self, slotId):
        '''
        Constructor
        '''
        self.__isCarParked = False
        self.__slotId = slotId

    def getSlotId(self):
        '''
        The method to get the slot id
        '''
        return self.__slotId

    def parkCar(self):
        '''
        The method is to set the park-car-flag to true
        '''
        self.__isCarParked = True

    def leaveCar(self):
        '''
        The method for cars leaving
        '''
        self.__isCarParked = False

    def checkIfCarParked(self):
        '''
        The method is to check if the space has a car parking here
        '''
        return self.__isCarParked;
