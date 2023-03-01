#ex1
"""
1.Create a generator that generates the squares of numbers up to some number N.
"""
n = int(input())
squares_generator = (i * i for i in range(n))
for i in squares_generator:
    print(i, end =" ")
