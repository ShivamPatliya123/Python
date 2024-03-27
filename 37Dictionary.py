info={"Name":"Shivam","Age":20,"Id":57,"College":"CDGI"}
print(info)
print(type(info))
print(info["Name"])

print(info.keys())

for key in info.keys():
    print(info[key])

    print(f"The value corresponding to the key {key} is {info[key]}")

print(info.items())
for key,value in info.items():
    print(f"The value corresponding to the key {key} is {value}")

#Dictionary methods()

#Update()

M={122:45,123:89,553:69}
m={222:76,566:90}
M.update(m)
print(M)

# clear()

info={"Name":"Shivam","Age":20,"ID":57}
info.clear()
print(info)

#pop() / popitem()

M={122:45,123:89,553:69}
# M.pop(122)
# print(M)
M.popitem()#last Key and value remove in popitem
print(M)
