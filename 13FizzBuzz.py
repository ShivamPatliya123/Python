def fizzBuzz(r):
    for i in range(1,r):
        if(i%2==0 and i%6==0):
            print(str(i) +" = FizzBuzz")
        else:
            if(i%2==0):
                print(str(i) +" = Fizz")
            else:
                if(i%6==0):
                    print(str(i) +" = Buzz")
                else:
                    print(str(i))
fizzBuzz(51)
