#ex3
"""
Define a function with a generator which can iterate the numbers,
 which are divisible by 3 and 4, between a given range 0 and n.
"""
def numbers(a):
    for i in range(0, a+1):
        if i%3 == 0 and i%4 == 0:
            yield i
for i in numbers(int(input())):
    print(i, end = ' ')
