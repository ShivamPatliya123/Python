# without  argument

def greet (fx):
    def mfx():
        print("Good Morning")

        fx()
        print("Thank you for using this function")
    return mfx
    
@greet 
def hello():
    print("Hello World")
    
hello()


# with Argument

def ARG(x):
    def y(*args,**kururgs):
        print("hello")

        x(*args,**kururgs)
        print("exicute program")

    return y

@ARG

def add(a,b):
    print(a+b)

add(5,6)
