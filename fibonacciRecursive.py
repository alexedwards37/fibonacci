#This is a Python file created in order to produce a Fibonacci sequence
#Written by Alex Edwards
#Date: 10/7/2019

#Initiates function.
def fibonacci(n):
    #ends function if value is below 0
    if n < 0:
        return 1
    else:
       #Creates the fibonacci sequence
       return(fibonacci(n-1) + fibonacci(n-2))
#The number of values in the suquence
value = 10
#Prints each value in the fibonacci sequence
for i in range(value):
    print(fibonacci(i-2))
