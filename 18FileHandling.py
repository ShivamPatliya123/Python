with open("file.text","r+") as myfile:#r+ read and write both case to be run
    print(myfile.read())
    myfile.write("I am fine")
myfile.close()

with open("file.text","r") as myfile: # r only for read the file
    print(myfile.read())
myfile.close()

with open("file.text","w") as myfile:
   # print(myfile.write())
    myfile.write("Hello shivam")
myfile.close()
