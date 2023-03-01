#ex5
"""
Implement a generator that returns all numbers from (n) down to 0.
"""
def allnum(z):
    for i in range(z, -1, -1):
        yield i 

for i in allnum(int(input())):
    print(i, end =' ')
