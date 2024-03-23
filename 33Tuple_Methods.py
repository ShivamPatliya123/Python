t=(1,2,4,12,33,42,'green')
print(type(t),t)
print("length of tupel",len(t))
print(t[0])
print(t[3])
print(t[4])
print(t[5])
print(t[-4])
print(t[len(t)-4])


if 6 in t:
    print("YES number present in this tuple")
else:
    print("number is not present in this tuple")

t1=t[:4]
print(t1)


#append()

countries=("India","Spain","Italy","England")
temp=list(countries)
temp.append("Russia")
temp.pop(3)
temp[2]="ShriLanka"
countries=tuple(temp)
print(countries)

#count()

num=(1,2,3,1,2,4,2,1)
print(num.count(2))

#index()

num=(1,2,3,1,2,4,2,1)
print("number present index is :",num.index(2,2,6))
