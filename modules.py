def sum(a,b):
    print(f"This is sum Number: {a+b}")
    
def inv(a,b):
    print(f"That is inv num: {a-b}")

    
def mal(a,b):
    print(f"That is maltipul num: {a*b}")

    
def dev(a,b):
    print(f"That is div num: {a/b}")
#===========================================================================
   
def trang(a,b):
    print(f"that is sum {a+b}")

def win(c,d):
    print(f"that is inv num {c-d}")

#===========================================================================
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

