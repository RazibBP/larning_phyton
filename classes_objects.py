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
    name = ''
    email = ''
    password = ''
    login = False

    def login(self):
        email = input ("Enter your Email :")
        password = input("Enter your password : ")

        if email == self.email or password == self.password:
            login = True
            print("Login successful")
        else:
            print("Login faild")

    def log(self):
        login = False
        print("Log out ")

    def inlogin(self):
        if self.login:
            return True
        else:
            return False
    
    def profile(self):
        if self.inlogin():
            print(self.name, "-" ,self.email)
        else:
            print("user is not log in ")

user1 = user()
user1.name = "Tahsin Hossan"
user1.email = "mdrazib.dev@gmail.com"
user1.password = 12345

user1.login()
user1.profile()

    