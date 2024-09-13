class student:
    Name = ""
    Roll = ""
    Ago = ""
    City = ""
    Result = ""


collage = student()
collage.Name = "Tahsin"
collage.Roll = 101
collage.Ago = 20
collage.City ="Madaripur"
collage.Result = 4.07

print(f"Roll : {collage.Roll}")
print(f"Name : {collage.Name}") 
print(f"Ago : {collage.Ago}")
print(f"Result : {collage.Result}") 
print(f"City : {collage.City}")

class user():
    email = ''
    name = ''
    password = ''
    #is_login = False

    def login(self):
        email = input ("Enter your Email :")
        password =int( input("Enter your password : "))

        if  email == self.email  and password == self.password:
            print("Login successful")
        else:
            print("Login faild")

    def log(self):
        is_login = False
        print("Log out ")

    def hasLogin(self):
        if self.is_login:
            return True
        else:
            return False
    
    def profile(self):
        if self.hasLogin():
            print(self.name, "-" ,self.email)
        else:
            print("user is not log in ")

user1 = user()
user1.name = "Mr.Tahsin"
user1.email = "mdrajibbp@gmail.com"
user1.password = 312132

user1.login()
#user1.log()
#user1.hasLogin()
user1.profile()

    
class person():
    name = ""
    age = ""

p1 =  person()
p1.name = "Johan"
p1.age = 36

print(f"Name: {p1.name}")
print(f"Ago :{p1.age}")

def some(x = 0):
    return x

print(some(20))

a = float(input())
b = float(input())
d = (a + b)
c = (d / 2)
print("MEDIA = %0.5f" %c)