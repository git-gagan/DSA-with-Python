#Program for Binary Search for sorted array input

#Iterative Implementation...
def bSearchIterative(l,x,start,end):
    # Worst Case Time complexity O(logn), auxiliary space is O(1)
    while start <= end:
        mid = (start + end)//2
        if x == l[mid]:
            return f'Element found at index {mid}'
        elif x < l[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return "Element is not in the array!"

#Recursive Implementation
def bSearchRecursive(l,x,start,end):
    #Worst case time complexity is O(logn), BUT auxiliary space required is O(n) (Call Stack)
    if start > end:
        return "Element is not in the array!"
    mid = (start + end)//2
    if l[mid] == x:
        return f"Element found at index {mid}"
    elif l[mid] > x:
        end = mid - 1
    else:
        start = mid + 1
    return bSearchRecursive(l,x,start,end)

inp_list = list(map(int,input("Enter Sorted array values : ").split()))
x = int(input("Enter the element to be searched : "))
start,end = 0, len(inp_list) - 1
res1 = bSearchIterative(inp_list,x,start,end)
res2 = bSearchRecursive(inp_list,x,start,end)
print("Res1 : ",res1,"\nRes2 : ",res2)