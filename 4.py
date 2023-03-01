#ex4
"""
Implement a generator called squares to yield the square of all numbers from (a) to (b). 
Test it with a "for" loop and print each of the yielded values.
""" 
x = int(input())
y = int(input())  
def all_number(x, y):
    for i in range(x, y + 1):
        yield i**2

for i in all_number(x, y):
    print(i, end = " ")  
