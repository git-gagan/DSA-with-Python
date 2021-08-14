#Introduction to Lists
"""
Lists are the most basic data structure used in python.
Advantages:
heterogenous, random access, cache friendly, dynamic Size
Disadvantages:
Slow insertion, deletion and search operation
"""

#Program to find mean/average of a list
def average():
    my_sum = 0
    for ele in inp_list:
        my_sum += ele
    return my_sum/len(inp_list)
    # or return sum(inp_list)/len(inp_list)

if __name__ == "__main__":
    print("Enter the list size : ")
    n = int(input())
    inp_list = []
    for ele in range(n):
        inp_list.append(int(input(f'Element number {ele + 1}:')))
    print(average())