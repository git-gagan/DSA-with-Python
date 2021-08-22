#Program to find all the occurrences in a sorted list

#Optimized Implementation using first and last occurrence
def binary(l,x,start,end):
    first = firstoccurrence(l,x,start,end)
    if first == -1:
        return 0
    return lastoccurrence(l,x,start,end) - first + 1

def firstoccurrence(l,x,s,e):
    while s <= e:
        mid = (s + e)//2
        if l[mid] > x:
            e = mid - 1
        elif l[mid] < x:
            s = mid + 1
        else:
            if mid == 0 or l[mid] != l[mid-1]:
                return mid
            e = mid - 1
    return -1

def lastoccurrence(l,x,s,e):
    while s <= e:
        mid = (s + e)//2
        if l[mid] > x:
            e = mid - 1
        elif l[mid] < x:
            s = mid + 1
        else:
            if mid == len(l)-1 or l[mid] != l[mid+1]:
                return mid
            s = mid + 1

li = list(map(int,input("Enter values : ").split()))
x = int(input("Enter the element to search : "))
start,end = 0,len(li)-1
print(f"Number of occurrences of {x} is : {binary(li,x,start,end)}")