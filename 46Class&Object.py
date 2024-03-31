class person: # class define
    name = "shivam"
    roll_no = 57
    sem = 4
    branch = "AI&DS"
    def info(self):
        print(f"Name = {self.name} Roll_NO = {self.roll_no} sem = {self.sem} Branch = {self.branch}")
a = person() # object is a
a.info()
print("\n")

# one class use multiple time;

b = person() # object is b

b.name = "jay"
b.roll_no = 45
b.sem = 4
b.branch = "BCA" 
b.info()
