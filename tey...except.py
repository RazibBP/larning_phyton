print("hello World")
try:
    x =10
    y =20
    sum = x + y
    print(sum)
except TypeError:
    print("Type Eroor")

print("Hi! Every one.")

try:
    x  = input("Enter a namber:")
    b =  input("Enter a namber:")
    div = x/b
    print("Divition:",div)
except ZeroDivisionError:
    print("ZeroTypeError")
except TypeError:
    print("Type Error")

print("Hy I am Tahsin.")


try:
    x  = int(input("Enter a namber:"))
    b =  int(input("Enter a namber:"))
    div = x/b
    print("Divition:",div)
except ZeroDivisionError:
    print("ZeroTypeError")
#except TypeError:
    #print("Type Error")2

print("Hy I am Tahsin.")


try:
    list =[20,0,30,50]
    li1 = list[0]/list[1]
    print(li1)
except ZeroDivisionError:
    print("ZeroTypeError:")
finally:
    print("Exact This print is run")


try:
    x  = int(input("Enter a int Namber:"))
    y = int(input("Enter a int Namber:"))
    z = x/y
    print(z)
except ValueError:
    print("Valu type Error")

