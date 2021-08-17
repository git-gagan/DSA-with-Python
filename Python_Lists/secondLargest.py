def secondLargestNaive(li):
    #Naive Solution
    if not li:
        return None
    maximum = li[0]
    for ele in li:
        if ele > maximum:
            maximum = ele
    secondmax = None
    for ele in li:
        if ele != maximum:
            if secondmax == None:
                secondmax = ele
            else:
                secondmax = max(ele,secondmax)
    return secondmax

def secondLargestoptimized(li):
    #Optimized
    if not li:
        return None
    largest = li[0]
    secondlargest = None
    # [ 3,4,5,6,1]
    for ele in li:
        if ele > largest:
            secondlargest = largest
            largest = ele
        if ele != largest:
            if secondlargest == None or ele > secondlargest:
                secondlargest = ele
    return secondlargest
        
        
inp_list = list(map(int,input("Enter the list values: ").split()))
print("Second largest element is: ",secondLargestNaive(inp_list))
print("Second largest element is: ",secondLargestoptimized(inp_list))