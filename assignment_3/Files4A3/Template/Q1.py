"""
                University of Canberra
        Programming for Data Science G (11521) - 2022 (S2)
                    Assignment 3

Question 1 [4 marks] (Lectures): Apply Index and Slice Operation to list x below to have lists y, z, t and u.
Add your code to y, z, t and u (# missing code) to implement this task in the program below.

The complete program without missing code will output the following:
x = [[6, 9, 12, 15], [8, 12, 16, 20], [10, 15, 20, 25], [12, 18, 24, 30], [14, 21, 28, 35], [16, 24, 32, 40]]
y = [[8, 12, 16, 20], [10, 15, 20, 25]]
z = [[12, 18, 24, 30]]
t = [[14, 21, 28, 35], [6, 9, 12, 15]] u = [12, 18]

FAQs:
1. Can I import external libraries, for example numpy?
No, you can not import external libraries for this question

2. Is it necessary to use array indexing and slicing?
Yes. The trivial solution, say for y is y = [[8, 12, 16, 20], [10, 15, 20, 25]], and then print('y = ', y).
Of course, this is NOT what we are looking for, and NO MARKS will be awarded for such solutions.

3. Will I get partial marks if there's a bracket missing?
If there are brackets missing or similar outputs which are different from the ones asked,
 partial marking will NOT be given. 
 
Marking rubric:
    
y - 1 Mark
z - 0.5 Marks
t - 1 Mark
u - 1.5 Marks

"""

x = [[a*b for a in range(2, 6)] for b in range(3, 9)]
y = # missing code
z = # missing code
t = # missing code
u = # missing code
print('x =', x)
print('y =', y)
print('z =', z)
print('t =', t)
print('u =', u)
