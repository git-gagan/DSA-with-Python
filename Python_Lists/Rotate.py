#Program to rotate a list by d places in both left and right direction!
def left(l,d):
    # Direct Methods:
    # return l[d:] + l[0:d]
    # or
    # l.append(l.pop(0))
    #Logical Method :-
    res = []
    for i in range(len(l)):
        res.append(l[(i+d)%len(l)])
    return res

def reverse(l, left, right):
    while left < right:
        l[left],l[right] = l[right], l[left]
        left += 1
        right -= 1

def leftoptimized(li, d):
    #for right rotation, pass n-d
    # if d = 2, then [ 1,2,3,4,5 ] -> [2,1,3,4,5] -> [2,1,5,4,3] -> [3,4,5,1,2]
    reverse(li,0,d)
    reverse(li,d+1,len(li)-1)
    reverse(li,0,len(li)-1)
    return li
    
inp_list = list(map(int,input("Enter input Values of the list: ").split()))
d = int(input("Places to rotate: "))
print("New list : ",leftoptimized(inp_list,d))