class Ticket(object):
    '''
    This class is the parking ticket
    '''
    __slotId = 0
    __registratonNumber = None
    __age=None
    def __init__(self, slotId, registratonNumber,age):
        '''
        Constructor
        '''
        self.__slotId = slotId
        self.__registratonNumber = registratonNumber
        self.__age = age

    def getSlotId(self):
        '''
        The method to get the slot id
        '''
        return self.__slotId

    def getregistratonNumber(self):
        '''
        The method to get the registration number
        '''
        return self.__registratonNumber
    def getage(self):
        '''
        The method to get the car age
        '''
        return self.__age

    def setRegistratonNumber(self,registratonNumber):
        '''
        The method is to set the registration number
        '''
        self.__registratonNumber = registratonNumber

    def setAge(self,age):
        '''
        The method is to set the car age
        '''
        self.__age = age
