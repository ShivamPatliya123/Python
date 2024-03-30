f = open("file.text",'r')
text = f.read()
print (text)
f.close()



with open('my_name.text','w') as f:
    f.write("hey my name is shivam patliya")
f.close()
