class Patient:
    def __init__(self , name , disease , age:int):
        self.__name = name
        self.__disease = disease
        self.__age = age
    
    #GETTERS
    def getName(self):
        return self.__name
        
    def getDisease(self):
        return self.__disease
        
    def getAge(self):
        return self.__age
        
    #SETTERS
    def setName(self, newName):
        self.__name = newName
    
    def setDisease(self, newDisease):
        self.__Disease = newDisease
    
    def setAge(self, newAge):
        self.__age = newAge
    
    
    #PRINT METHOD
    def displayInfo(self):
        print(f'Name : {self.__name}')
        print(f'Disease : {self.__disease}')
        print(f'Age : {self.__age}')
        
        
# Child Class
class InHousePatient(Patient):
    def __init__(self , name , disease , age:int , bed_no:int):
        super().__init__(name , disease , age)
        self.__bed_no = bed_no
        
    def getBedNo(self):
        return self.__bed_no
    
    def setBedNo(self, newBedNo):
        self.__bed_no = newBedNo
    
    def displayInfo(self):
        super().displayInfo()
        print(f'Bed Number : {self.__bed_no}')
    
# Chlild Class
class OutHousePatient(Patient):
    def __init__(self , name , disease , age , medicine):
        super().__init__(name , disease , age)
        self.__medicine = medicine

    def getMedicine(self):
        return self.__bed_no
    
    def setMedicine(self, newMedicine):
        self.__medicine= newMedicine

    def displayInfo(self):
        super().displayInfo()
        print(f'Medicine : {self.__medicine}')



op1 = OutHousePatient("ZZ" , "hemophilia" , 30 , "Saari")
op1.displayInfo()
print()
op2 = InHousePatient("Zhumail" , "malaria" , 18 , "2 Bed")
print(op2.getBedNo())
print()
p1 = Patient("ibad" , 'Flu' , 16)
p1.displayInfo()