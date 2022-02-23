    
#palindrome

def palindrome(p):
    if(p==p[::-1]):
        print("TRUE, it is palindrome")
    else:
        print("FALSE ,it is not a palindrome")

#main
p=str(input("Enter the Number:"))
palindrome(p)
