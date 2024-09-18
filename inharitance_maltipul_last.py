class A:                                #parant class
    def  __init__(self ,name):
        self.name = name
        self.color = "blue"

    def show(self):
        print("Name: ",self.name,"is looking good for",self.color,"T_Shart")

class B:                                #parant class
    def __init__(self,name):
        self.name = name
        self.color = "White"

    def show1(self):
        print(self.name,"is looking vary cool is",self.color,"t_shart")

class C(A,B):
    def __init__(self,name,):
        super().__init__(self,"Tahsin")
       # self.color = "green"


    def show2(self):
        print(self.name,"is not vary good looking but some good look is",self.color,"t_shart.When",self.name,"is try ",self.color," t+thart bater than looking good")

c1  = C("Rihab")
c1.show2()
#c1.show1()
#c1.show()
