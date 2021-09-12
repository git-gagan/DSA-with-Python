#Sum of First N natural numbers using recursion
def sum(n):
    #If number is 0 return 0
    if n == 0:
        return n
    #else return sum of given number plus previous number
    return n + sum(n-1)
    #OR simply use the formula :- n*(n+1)/2

n = int(input("Enter the number till which sum needs to be found : "))
print(sum(n))