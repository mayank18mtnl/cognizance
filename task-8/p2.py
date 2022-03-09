# check if arrays are same

import numpy as n

def eqary():
    x=n.random.randint(0,2,6)
    print("First array",x)
    y=n.random.randint(0,2,6)
    print("First array",y)
    print("wether the arrays are equal or not ! ")
    eql=n.allclose(x,y)
    print(eql)

eqary()
