def cube(x):
    return x*x*x
print(cube(8))

l = [9,2,4,6,4,3]
l.sort()
print(l)
new=list(map(cube,l))
print(new)
l.reverse()
print(l)
new=list(map(cube,l))
print(new)
