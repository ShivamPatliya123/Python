#Break Statement

for i in range(1,10,1):
    
    if(i==8):
        print("Break statment exicuit")
        break
    else:
        print(i,end=" ")
        print()
        
# Continue Statement

for i in [5,3,12,6,8,9]:
    if(i%2==0):
        continue
    print(" element not reminder ZERO=",i)
