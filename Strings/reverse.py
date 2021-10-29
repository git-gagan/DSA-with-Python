#Reverse of a string in python
def rev(s):
    print("Reversed string through one-liner : ",s[::-1])
    rev_str = ""
    for i in s:
        rev_str = i + rev_str
    print("Reversed string through loop : ",rev_str)

s = input("Enter string here : ")
rev(s)