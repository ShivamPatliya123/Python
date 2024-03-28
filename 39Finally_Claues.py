def func1():
    try:
        l=[1,4,3,2]
        i = int (input("enter the index:"))
        print(l[i])
        return 1
    except:
        print("some error occured")
        return 0
    finally:
        print("I am always executed")
x=func1()
print(x)

# short hand if else statement

a = 330
b = 3
print("A")if a>b else print("==") if a==b else print("B")
