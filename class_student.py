class student:
    count =0
    univarcity = "Dafotil univaercity"
    def __init__(self ,name , Id) -> None:
        self.name  = name
        self.Id  = Id
        student.count +=1
        #student.univarcity

    def detailscd(self):
        print(student.univarcity,"Total student: ",student.count)
        print("Id: ",self.Id,"Name: ",self.name)
        #print("Id: ",self.Id,"Name: ",self.name)
        #print("Total student: ",student.count)

    @classmethod
    def up_new_name(cls,u_new_name):
        cls.univarcity = u_new_name


#==========================================================

s1 = student("Rajib" , "101")
s2 = student("Tahsin" , "102")
s3 = student("Rihab" , "103")
s4 = student("Rahim" , "104")
student.up_new_name("BRAC UNIVERCITY")
s1.detailscd()
s2.detailscd()
s3.detailscd()
s4.detailscd()

