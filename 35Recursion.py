def factorial(num):
    if(num==1 or num==0):
        return 1
    else:
        return(num*factorial(num-1))
num=6
print("number:",num)
print("factorial:",factorial(num))

#fibonacci series

def fibonacci(n):
    if (n<2):
        return n
    else:
        return (fibonacci(n-1)+fibonacci(n-2))
n=int(input("Enter a non negative number:"))
if n<0:
    print("fibonacci number are undefined for negative number")
else:
    print("fibonacci number at position",n,"is",fibonacci(n))
