info={'carlo',2,21,"string",37}
print(info)
print(type(info))


# set method()
# union() 

cities1={"Indore","Bhopal","Khargoan","Sanavad","Barwaha"}
cities2={"Pithampure","Bediya","Indore","Bhopal"}
cities3=cities1.union(cities2)
print(cities3)

# intersection() / intersection_update()

cities1={"Indore","Bhopal","Khargoan","Sanavad","Barwaha"}
cities2={"Pithampure","Bediya","Indore","Bhopal"}
cities3=cities1.intersection(cities2)
print(cities3)

cities1={"Indore","Bhopal","Khargoan","Sanavad","Barwaha"}
cities2={"Pithampure","Bediya","Indore","Bhopal"}
cities1.intersection_update(cities2)
print(cities1)

# symmetric_differnce() / symmetric_difference_update()

cities1={"Indore","Bhopal","Khargoan","Sanavad","Barwaha"}
cities2={"Pithampure","Bediya","Indore","Bhopal"}
cities3=cities1.symmetric_difference(cities2)
print(cities3)

cities1={"Indore","Bhopal","Khargoan","Sanavad","Barwaha"}
cities2={"Pithampure","Bediya","Indore","Bhopal"}
cities1.symmetric_difference_update(cities2)
print(cities1)

# isdisjoint()

num={1,2,45,63,2}
num1={6,3,8,12,43}
print(num.isdisjoint(num1))

# issuperset()

num1={1,2,3}
num2={4,5,6}
num3={1,2,3}
print(num1.issuperset(num3)) #both set values are same
print(num3.issubset(num2))

# add()

colors={"Red","Green","Yellow","voilet"}
colors.add("Orange")
print(colors)

# Remove()

colors={"Red","Green","Yellow","Voilet"}
colors.remove("Green")
print(colors)

# pop()

names={"Shivam","Pawan","Jay","Manas"}
item=names.pop()
print(names)
print(item)
