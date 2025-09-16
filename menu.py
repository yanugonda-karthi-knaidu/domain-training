def square():
    print(a*a)
def rectangle(a,b):
    print(a*b)
def circle():
    return 3.14*a*a
def triangle(a,b):
    return 0.5*a*b

while(True):
    print("menu")
    print("1.square ")
    print("2.rectangle ")
    print("3.circle ")
    print("4.triangle ")
    print("5.exit ")
    choice=int(input("enter your choice: "))
    if choice==1:
        a=int(input("enter side of square: "))
        square()
    if choice==2:
        a=int(input("enter length of rectangle: "))
        b=int(input("enter breadth of rectangle: "))
        rectangle(a,b)
    if choice==3:
        a=int(input("enter the radious a :"))
        b=circle()  
        print(b)
    if choice==4:
        a=int(input("enter base of triangle: "))
        b=int(input("enter the height "))
        c=triangle(a,b)
        print(c)
    if choice==5:   
        break
    
