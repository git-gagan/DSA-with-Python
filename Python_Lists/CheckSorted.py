#Check if a given list is sorted or not!
#Naive way is to compare list with it's sorted version and return the corresponding bool value.

def checkSort(li):
    for i in range(len(li)-1):
        if li[i+1] < li[i]:
            return "UNSORTED"
    return "SORTED"

inp_list = list(map(int,input("Enter List Values : ").split()))
print(f'The list is :  {checkSort(inp_list)}')
