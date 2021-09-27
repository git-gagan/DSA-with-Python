#Sum of Digits of first N natural Numbers
def sumofdigits(n):
    if n < 10:
        return n
    return n%10 + sumofdigits(n//10)

N = int(input("Enter the Number : "))
print(sumofdigits(N))