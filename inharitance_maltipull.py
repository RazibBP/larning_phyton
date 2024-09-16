class student:
    def __init__(self,name,Id):
        self.name = name
        self.Id = Id

    def Detailse(self):
        print("Name: ",self.name,"ID: ",self.Id)

class CSEStudent(student):
    def __init__(self,name,Id,labs):
        super().__init__(name,Id)
        self.labs = labs

    def Cry(self):
        print("CSE Student All time is craying for",self.labs,"Labs(s)")


class CSEStudent_Felors(CSEStudent):
    
    def enrol_CSE110(self):
        print(self.name,"CSE Student is Enrol 110")


#===============================================================================

s1 = CSEStudent("Tahsin",101,3)
s2 = CSEStudent_Felors("Rihab",102,1)
s2.Detailse()
s2.Cry()
s2.enrol_CSE110()
s1.Detailse()
s1.Cry()