#Program to find first occurrence of an element in a sorted list!

#Naive Solution
#It doesn't take into account the fact that the list is sorted!
def linear(l,x):
    for i in range(len(l)):
        if l[i] == x:
            return "Element found at index {}".format(i)
    return "Element doesn't exist in the array."

#Optimized solution
def binary(l,x):
    start, end = 0, len(l) - 1
    while start <= end:
        mid = (start + end)//2
        if l[mid] == x:
            #If we are either at first location or there's no similar element on left, return
            if mid == 0 or l[mid - 1] != l[mid]:
                return f"Element found at index : {mid}"
            else:
                #Check for left half in the array
                end = mid - 1
        elif l[mid] > x:
            end = mid - 1
        else:
            start = mid + 1
    return "Element is not in the array!"

lis = list(map(int,input("Enter the list values : ").split()))
x = int(input("Enter the element to be searched : "))
print(binary(lis,x))