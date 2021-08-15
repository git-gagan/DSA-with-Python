"""
Python Program to segregate a list of elements depending on whether they are even or odd
"""

def sepEvenOdd(li):
    even, odd = [], []
    for ele in li:
        even.append(ele) if ele%2 == 0 else odd.append(ele)
    return even, odd

inp_list = map(int,input("Enter the numbers ").split())
even_list, odd_list = sepEvenOdd(inp_list)
print("Even List: ",even_list,"\nOdd List: ",odd_list, sep="")