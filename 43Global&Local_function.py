x = 10 # its global variable
def my_function():
    y=5 # its local variable
    global x
    x=4 # change of global variable value
    print(y)
my_function()
print(x)
