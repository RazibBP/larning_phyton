#function command practice is start
def my_function():
    print("Hello World")
my_function()

def my_functuon(x , y):
    sum=(x+y)
    print(sum)
my_functuon(12 ,13)

def my_name(Name):
    print("This is my Name", Name)
my_name("Tahsin")
my_name("Razib")
my_name("Rihab")

def love(r , s):
    print(r + " + " + s)
love("Tahsin","Sumiya")
love("Rakib","Oithi")
love("Nirob","Ripti")
love("Onik","Sanjida")

def my_look(*kid):
    print("My Name is ", kid[1])
    print("My Best well Name Is ",kid[2])
my_look("Razib","Tahsin","Rihab")


def my_nickname(NAME):
    print("My Name is",NAME )
my_nickname("Tahsin")

def clas(study):
    print("I read in class",study)
clas("Honars 1st year")

def for_loop(foods):
    for x in foods:
        print(x)
fruts = ["Apple","Ball","Cat","Dog","Elefant","Fish"]
for_loop(fruts)

def reatun(x):
    return 5 * x
print(reatun(3))
print(reatun(5))

#function command practice all done 


#function lambda practice is start now

x = lambda a: a + 10
print(x(5))

x = lambda a,b,c: a + b + c
print(x(100,200,300))

def my_fun(n):
    return lambda a: a * n
sum = my_fun(5)
print(sum(10))

def doubl(n):
    return lambda a: a*n
sum = doubl(5)
ad = doubl(7)
print(sum(7))
print(ad(7))
