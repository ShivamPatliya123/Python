letter="Hey my name is {1} and i am from {0}"
country="India"
name="Shivam"

print(letter.format(country,name))

print(f"Hey my name is {name} and i am from {country}")


#Dostirng:

def square(n):
    '''Take in a number n,return the square of n'''
    print(n**2)
square(5)
print(square.__doc__)
