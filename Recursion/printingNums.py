#Printing 1 to N and N to 1
def onetoN(n):
    if n <= 0:
        return
    onetoN(n-1)
    print(n)

def ntoOne(n):
    if n <= 0:
        return
    print(n)
    ntoOne(n-1)

N = int(input("Enter the number : "))
onetoN(N)
ntoOne(N)