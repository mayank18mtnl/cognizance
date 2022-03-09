# add two numpy array

import numpy as n

def addarr():
        x=n.array(eval(input("Enter the array")))
        y=n.array(eval(input("Enter the array")))
        z=n.add(x,y)
        print("final added arrays is: ", z)

addarr()
