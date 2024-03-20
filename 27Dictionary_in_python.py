d={'Name':'python','Fees':8000,'Duration':'2month'}
print (d['Duration'])#access only specific value

print(d)

for i in d:
    print(i) #access key names
    print(d[i]) # access  value name

print(type(d))

# dictionary change into list


list(d.keys())
list(d.values())
print(d.items())
