#Recursive Solution for Tower of Hanoi Problem (Time Complexity :- O(2^n))
"""
Rules :-
1) Move only one disc at a time
2) Move only top disc
3) Only small Disc can be placed over larger one
"""

def toh(n,A,B,C):
    if n == 1:
        print(f"Move {n} to {C}")
    else:
        toh(n-1,A,C,B)
        print(f"Move {n} to {C}")
        toh(n-1,B,A,C)

n = int(input("Enter a positive interger : "))
toh(n,"A","B","C")