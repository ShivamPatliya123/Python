import random
year=random.randint(1992,2024)
print(year)
if(year%4==0 and year%100!=0 or year%400==0):
    print("Given year is a leap year")
else:
    print("Given year is a not leap year")
