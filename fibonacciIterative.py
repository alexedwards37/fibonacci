#This is a Python file created in order to produce a Fibonacci sequence
#Written by Alex Edwards
#Date: 10/7/2019

#Creates initial values
a,b,n = 0,1,0
#The number of values in the fibonacci sequence
value = 10
#Loop that creates the fibonacci sequence
while n < value:
        #print statement prints each value of the sequence
        print(b)
        #The code that adds the value to each number in the sequence
        a, b = b, a + b
        #adds value to the loop
        n += 1
