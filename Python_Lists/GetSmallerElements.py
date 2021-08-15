#Python Program to find smaller elements than the given number in a list

inp_list = map(int,input("Enter List elements : ").split())
x = int(input("Enter the number x : "))
res_list = [ele for ele in inp_list if ele < x]
print("Result : ",res_list)