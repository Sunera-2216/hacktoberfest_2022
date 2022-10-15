def floorSqrt(x):

 

    # Base cases

    if (x == 0 or x == 1):

        return x

 

    # Starting from 1, try all numbers until

    # i*i is greater than or equal to x.

    i = 1

    result = 1

    while (result <= x):

 

        i += 1

        result = i * i

 

    return i - 1

 

 



x = 11

print(floorSqrt(x))

 

# This code is contributed by Ramanujam 