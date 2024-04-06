class Employe:
    def __init__(self,name,id):
        self.name = name
        self.id = id
    def showdata(self):
        print(f"The name of employe : {self.name} \n and is id : {self.id}")

class programmer(Employe):
    def showlanguage(self):
        print("The default language is python")

e = Employe("Rohan Das",400)
e.showdata()
print()
e1 = programmer("Vijay",344)
e1.showdata()
e1.showlanguage()
