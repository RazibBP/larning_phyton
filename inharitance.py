class Animal:

    def __init__(self,name) -> None:
        self.name = name

    def eat(self):
        print(self.name,"is Eating")

class Dog(Animal):
    def bard(self):
        print(self.name,"is Sleping")

#=========================================================================

a1 = Animal("Jack")
b1 = Dog("Sumu")
b1.bard()
b1.eat()  
a1.eat()

#=========================================================================

class Student:
    def __init__(self,name,id) -> None:
        self.name = name
        self.id = id

    def Detailse(self):
        print("Name: ",self.name,"ID: ",self.id)

class CSCStudent(Student):
    def __init__(self,name,id,labs):
        super().__init__(name,id)
        self.labs = labs
    def cry(self):
        print("CSE Student  all time is crying because of",self.labs,"labs")

class BBAStudent(Student):
    def party(self):
        print("BBA S tudent All time do party")

#============================================================================================

s1 = CSCStudent("Tahsin",101,3)
s2 = BBAStudent("Rajib",102)
s1.Detailse()
s2.Detailse()
s1.cry()
s2.party()