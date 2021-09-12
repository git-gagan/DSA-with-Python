#Recursion to get floor of binary log of a number
def log(n):
    #Base Condition
    if n <= 1:
        return 0
    #Recursive Call
    return 1 + log(n//2)

#Recursion to find binary representation of a number
def binary(n):
    if n <= 0:
        return
    binary(n//2)
    print(n%2,end="")

n = int(input("Enter the number whose log base 2 needs to be found :"))
print("Log is : ",log(n))
binary(n)
