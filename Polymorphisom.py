class frist:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model

  def move(self):
    print("Move!")

class Car(frist):
  pass

class Boat(frist):
  def move(self):
    print("Sail!")

class Plane(frist):
  def move(self):
    print("Fly!")

car1 = Car("Tahsin","BMW") #Create a Car object
boat1 = Boat("Podma", "T 10") #Create a Boat object
plane1 = Plane("Arabiyan", "747") #Create a Plane object

for x in (car1, boat1, plane1):
  print(x.brand)
  print(x.model)
  x.move()