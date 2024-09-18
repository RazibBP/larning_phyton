class iterat:
    def __iter__(self):
        self.num = 1
        return self

   # def __iter__(self):
      #  return self
    
    def __next__(self):
        if self.num <=10:
            values = self.num
            self.num +=1
            return values
        else:
           raise StopIteration
FF = iterat()
#print(iterator)
FFF = iter(FF)
for x in FFF:
    print(x)

list = ["Tahsin","Rihab","Razib",1,2,3,4,5,6,7]

list1=iter(list)
print(list1.__next__())
print(list1.__next__())
print(list1.__next__())
print(list1.__next__())
print(list1.__next__())


class iterator:
  def __iter__(self):
    self.a = 1
    return self

  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration

FF = iterator()
myiter = iter(FF)

for x in myiter:
  print(x)