from Slot import Slot
from Ticket import Ticket

class ParkingLot(object):
    '''
    The class is the whole parking lot
    '''

    __slotreader = None
    __slotCount=0
    __slots = []
    __Tickts=[]

    def __init__(self,slotCount):
        '''
        Constructor
        '''
        slotstatus = True
        self.__slotCount = slotCount
        for i in range(self.__slotCount):
            slotNumber = i+1
            self.__slots.append(Slot(slotNumber))
            self.__slotreader = Slot(slotNumber)
            if self.__slots[i].getSlotId() == slotNumber and self.__slots[i].checkIfCarParked() == False:
               slotstatus = slotstatus = True
            else:
               slotstatus = slotstatus = False
        if slotstatus == True:
            print('Created a parking lot with {} slots'.format(self.__slotCount))

    def getAvailableSlot(self):
        '''
        The method is return nearest parking lot
        ''' 
        for i in range (self.__slotCount):
            if self.__slots[i].checkIfCarParked() == False:
               return self.__slots[i].getSlotId()

    def isSlotAvailable(self):
        '''
        The method to check if the parking lot allow is available
        '''
        for i in range (self.__slotCount):
            if self.__slots[i].checkIfCarParked() == False:
               return True
               break

        return False

    def parkThePark(self,slotId, registrationNumber,age):
        '''
        To park the car in the position
        '''
        for i in range(self.__slotCount):
            if self.__slots[i].getSlotId() == slotId:
               slotindex = i
               break
        if len(self.__Tickts) != self.__slotCount:
           self.__Tickts.append(Ticket(slotId, registrationNumber, age))
        else:
           self.__Tickts[slotindex].setRegistratonNumber(registrationNumber)
           self.__Tickts[slotindex].setAge(age)
        self.__slots[slotindex].parkCar()
        if self.__slots[slotindex].checkIfCarParked() == True:
            print("Car with vehicle registration", registrationNumber, "has been parked at slot number ", slotId)

    def leaveTheCar(self, slotId):
        '''
        The car leaves off the space
        '''
        for i in range(self.__slotCount):
            if self.__slots[i].getSlotId() == slotId:
               slotindex = i
               break
        self.__slots[slotindex].leaveCar()
        if self.__slots[slotindex].checkIfCarParked() == False:
            print('Slot number {} is free'.format(slotId))

    def showParkingStatus(self):
        '''
        The method to show the parking status of the parking lot
        '''
        print("Slot No.   Registration No.  Age")
        for i in range(self.__slotCount):
            if self.__slots[i].checkIfCarParked() == True:
                print(str(self.__Tickts[i].getSlotId()) + "           " + str(
                    self.__Tickts[i].getregistratonNumber()) + "       " + self.__Tickts[i].getage())

    def getRegistrationNumbersFoCarsWithColour(self,age):
        '''
        The method is to get registration numbers for parcular age
        ''' 
        cars=[]
        for i in range(self.__slotCount):
            if self.__slots[i].checkIfCarParked() == True and self.__Tickts[i].getage() == age:
               cars.append(str(self.__Tickts[i].getregistratonNumber()))

        print(", ".join(cars))

    def Vehicle_registration_number_for_driver_of_age(self,age):
            '''
            The method is to get registration numbers for particular age
            '''
            cars=[]
            for i in range(self.__slotCount):
                if self.__slots[i].checkIfCarParked() == True and self.__Tickts[i].getage() == age:
                   cars.append(str(self.__Tickts[i].getregistratonNumber()))

            print("Vehicle Registration Number with Driver's age of", age, "are : ")
            print(", ".join(cars))

    def Slot_numbers_for_driver_of_age(self,age):
        '''
        The method is to get slots numbers for parcular age
        '''
        cars=[]
        for i in range(self.__slotCount):
            if self.__slots[i].checkIfCarParked() == True and self.__Tickts[i].getage() == age:
               cars.append(str(self.__Tickts[i].getSlotId()))

        print("Slot Numbers with Driver's age of", age, "are : ")
        print(", ".join(cars))

    def getSlotNumberForRegistrationNumber(self,registartionNumber):
        '''
        The method is to get slots numbers for particular RegistrationNumber
        '''
        status=False
        for i in range(self.__slotCount):
            if self.__slots[i].checkIfCarParked() == True and self.__Tickts[i].getregistratonNumber() == registartionNumber:
               status=True
               break
        if status == True:
            print("Slot Number is: ", self.__Tickts[i].getSlotId())
        else:
            print("Not found")
           

    

    
        


        


        

