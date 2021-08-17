#Program to find the only element in list appearing odd number of times

def Naiveodd(li):
    #Naive Solution
    for ele in li:
        if li.count(ele) % 2 != 0:
            return ele

def Optimizedodd(li):
    #optimized solution using XOR
    # x ^ 0 = x, x ^ x = 0, irrespective of order!
    res = 0
    for ele in li:
        res = res ^ ele
    return res
        
inp_list = list(map(int,input("Enter the list values : ").split()))
print("Only number with odd occurrences is : ",Naiveodd(inp_list))
print("Only number with odd occurrences is : ",Optimizedodd(inp_list))