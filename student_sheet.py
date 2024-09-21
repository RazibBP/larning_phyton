class student:
    def __init__(self,Id,name,gender,ago) -> None:
        self.name = name
        self.Id = Id
        self.gender = gender
        self.ago = ago

    def Student_detailse(self):
        print("ID :",self.Id,"   ","Name :",self.name,"  ","Gander: ",self.gender," ","AGO: ",self.ago)



#s1  = student(101,"Tahsin","Male",20)
#s1.Student_detailse()