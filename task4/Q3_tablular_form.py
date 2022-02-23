
#creating record table ,printing it and print the required record 

from tabulate import tabulate
l=[]
def add():
    i=int(input("Enter the number of student :"))
    for i in range(0,i):
        r=int(input("Student Roll Number :"))
        n=str(input("Student name :"))
        m=int(input("Student Marks :"))
        x=[r,n,m]
        l.append(x)
    print(tabulate(l, headers=["Roll NO.","Name","marks"]))    
    print("")
    j=int(input("Enter the roll no to print record. "))
    for i in range(0,len(l)):
        if j==l[i][0]:
            print(l[i])

add()        
