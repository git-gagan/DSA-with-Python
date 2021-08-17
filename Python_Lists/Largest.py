#Program to find largest element in a list, can be optimized to get the minimum element too.

def largest(l):
    if len(l) == 0:
        return "Empty List"
    maximum = l[0]
    for ele in l:
        if ele > maximum:
            maximum = ele
    return maximum
        
li = list(map(int,input("Enter list values : ").split()))
max_element = largest(li)
print("Maximum Element in the list is:",max_element)