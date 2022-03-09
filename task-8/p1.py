# inserting 0s in betweeen arrays of number


import numpy as n

def inszero():
    x=n.array(eval(input("Enter the array")))
    y=5
    newx=n.zeros(len(x)+(len(x)-1)*(y))
    newx[::y+1]=x
    print("\nNew array:")
    print(newx)

inszero()
