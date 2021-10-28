#In Josephus problem, we have got a circle with n people and a parameter k. At each iteration we have to kill the 
#kth person from the given position till only one person remains. The target is to return the pos of survivor.

#Time Complexity :- O(n)
#Space complexity :- O(n)

#For 1-based indexing
def josephus(n,k):
    if n == 1:
        return 1
    #Call the josephus function to get the 1 to n values which survived
    x = josephus(n-1,k)
    #Map the x values to y to get the required surviving position.
    y = (x+k-1)%n+1
    return y

def josephus1(li,start,k):
    #Create a list and remove every kth position and return the last value
    if len(li) == 1:
        return li[0]
    start = (start+k-1)%len(li)
    li.remove(li[start])
    return josephus1(li,start,k)

n,k = map(int,input().split())
print("Survivor Position : ",josephus(n,k))
li = [i for i in range(1,n+1)]
start = 0
print("Survivor Position : ",josephus1(li,start,k))