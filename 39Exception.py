a=(input("Enter the number:"))
print(f"multiplication table of {a} is:")

try:
    if(int(a)>0):
        for i in range(1,11):
            print(f"{int(a)} X {i} = {int(a)*i}")
    else:
        print("Negative number")
except:
    print("invalid input!")
print("end of program")
