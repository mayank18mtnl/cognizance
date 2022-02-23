
#print traingle of given dimensions 


def tri():
    a=int(input("Give the number of rows:"))
    b=a-1
    for i in range(0,a):
        for j in range(0,b):
            print(end=" ")
        b=b-1
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")

tri()
