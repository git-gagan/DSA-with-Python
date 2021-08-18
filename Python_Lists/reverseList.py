#Program to reverse a list

def reverse_list(li):
    # Method 1
    # return list(reversed(li)), or li[::-1]
    # Method 2
    # li.reverse()
    # return li
    # Method 3
    i = 0
    j = len(li) - 1
    while i < j:
        li[i],li[j] = li[j],li[i]
        i += 1
        j -= 1
    return li

inp_list = list(map(int,input("Enter List Values : ").split()))
print(reverse_list(inp_list))