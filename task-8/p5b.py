# print identity matrix

import numpy as n

def idty():
    a=int(input("Enter Rows of square matrix :
                "))
    x=n.identity(a)
    print("\n MATRIX IS : \n",x)

idty()
