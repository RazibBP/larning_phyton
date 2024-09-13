class programar():
    def __init__(self) -> None:
        self.name = input("Enter your name :")
        self.Id = int (input("Enter your ID :"))
        self.selary = float(input("Enter your salary :"))

    def all_function(self):
        print("Name :" ,self.name)
        print("ID :" ,self.Id)
        print("Salary :" ,self.selary)

user1=programar()
user1.all_function()


