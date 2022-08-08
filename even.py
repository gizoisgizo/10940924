def averageEven(n) :
    n = 10

 

    if (n % 2 != 0) :

        print("Invalid Input")

        return -1

     

    sm = 0

    count = 0
 

    while (n >= 2) :
 

        # count even numbers

        count = count + 1
 

        # store the sum of even

        # numbers

        sm = sm + n
 

        n = n - 2

     

    return sm // count
 

n = 10

print(averageEven(n))