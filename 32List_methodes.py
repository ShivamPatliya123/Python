# append()

l=[2,34,6,3,2]
print(l)
l.append(8)
print(l)

# sort()

l=['voilet','indigo','yellow','blue']
print(l)
l.sort()
print(l)

# reverse()

num=[45,62,12,6,74,8]
num.reverse()
print(num)

# indexing()

colors=['red','yellow','blue','indigo','voilet']
print("index of colour blue is",colors.index('blue'))

# count()

num=[1,3,5,2,1,7,2,1,1]
print(num.count(1))

# copy()

l=[11,31,23,12,42,45]
print(l)
m=l.copy()
m[0]=0
print(l)
print(m)#value insert only for copy list not change in original list

#insert()
l=['bus','car','bike','train']
l.insert(0,'airoplane')
print(l)

#concatenation()
l=['red','yellow','orange','black']
m=[1,23,44,3,123,4]
print(l+m)
