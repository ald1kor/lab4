#ex2
"""
Write a program using generator to print the even numbers
 between 0 and n in comma separated form where n is input from console.
"""
def even_number(c):
    for i in range(0, c+1):
        if i%2 == 0:
            yield i
for k in even_number(int(input())):
    print(k, end = ',')
