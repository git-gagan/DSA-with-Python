#Program to find the last occurrence of an element in an array
#Optimized approach...
def binary(l,x):
    start, end = 0,len(l) - 1
    while start <= end:
        mid = (start + end)//2
        if l[mid] > x:
            end = mid - 1
        elif l[mid] < x:
            start = mid + 1
        else:
            if mid == len(l) - 1 or l[mid + 1] != l[mid]:
                return "Element found at index : {}".format(mid)
            start = mid + 1
    return "Element is not in the array!"

li = list(map(int,input("Enter list values: ").split()))
x = int(input("Enter the value to be searched : "))
print(binary(li,x))