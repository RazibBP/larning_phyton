a = 30
b = 50

if a > b:
    print("A Gater than B")
elif a < b:
    print("A less than B")
else:
    print("A or B equal")

x = 330
y = 300
z = 400

if x < y and y < z:
    print("x gater than y and y gater than z")
elif z < y and y < x:
    print("Z is gater than Y and Y is gater than x")
elif x == y and y == z:
    print("X equal is Y and Y equal Z")
elif y < x and x < z:
    print("Y gater than is X and X is gater than Z")
else:
    print("aLL tARM iS rOANG")

x = 50
y = 60
z = 70

if x < y or y < z:
    print("At lest on condition is true")

i =1
while i<10:
    sum = (5 * i)
    print(sum)
    i +=1

x = 100
y = 50
if not x < y:
    print ("That is true")