print("Log In")
data = input("Enter your youser ID: " )
gam = input("ENter your gmail account: ")

class student():
    def __init__(self,userid,gmail) -> None:
        self.userid = userid
        self.gmail = gmail
    
    
    def login(self):
        if self.userid == data and self.gmail == gam:
           # print("Enter your user ID:",self.userid)
           # print("Enter your Gmail Account: ",self.gmail)
           print("Login Successful")
        else:
            print("Lgin Faild")

#s1 = student("mdrajibbp@gmail.com","Tahsin")
#s1.input()
#s1.login()
s1 = student("Tahsin","mdrajibbp@gmail.com")
s1.login()