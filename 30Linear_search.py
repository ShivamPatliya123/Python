def linear_search(n,x):
    element=[]
    for i in range(1,n):
        element.append(i)
    count=0
    flag=0
    for i in element:
        count +=1
        if(i==x):
            print("YES !! found number is position"+str(i))
            flag=1
            break
        if(flag==0):
            print("number is not found")
        print("number of iteration:"+str(count))
linear_search(5,3)
