#default argument

def average(a=9,b=4):
    print("The average is",(a+b)/2)
average()

def average(a=4,b=8):
    print("The average is",(a+b)/2)
average(8,3)

def average(a=8,b=10):
    print("The average is",(a+b)/2)

average(a=6)#a defalut value not exicute
average(b=6)#b default value not exicute


# Key argument

def name(fname,id,age):
    print("hello",fname,id,age)
name(fname="XYZ",age=21,id=1)

#Required Argument

def name(fname,mname,lname):
    print("Hello",fname,mname,lname)
#name("XYZ","ABC")#error create
name("XYZ","ABC","PQR")

#Variable length argument

def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("Average is:",sum/len(numbers))
average(5,6,2)

def name(**name):
    print(type(name))
    print("Hello",name['fname'],name['mname'],name['lname'])
name(mname='XYZ',lname='ABC',fname='PQR')

#Return statement

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)

c=average(5,3,6)
print("The average is",c)
