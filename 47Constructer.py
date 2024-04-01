class info:

    def __init__(self,name,occ,id) -> None:
        self.name = name 
        self.occ = occ
        self.id = id

    def into (self):
        print(f"{self.name} is a {self.occ} and id_no is {self.id}")

a = info("shivam","Developer",57)
b = info("pawan","developer",43)

a.into()
print()
b.into()
