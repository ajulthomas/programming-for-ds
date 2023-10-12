# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 10:30:18 2021

*** Programming for Data Science ****

Examples Week 9 - Numpy and Matplotlib

@author: Dr. Raul Fernandez-Rojas
"""

# Definde working directory
import os
os.chdir('D:\\Files\\Raul\\Python\\PDS\\')  #selec *your own* working directory


#*************** Numpy *****************

# Example 1
import numpy as np

# 1D array
list1 = [1, 2, 3, 4, 5]
array1 = np.array(list1)
print('List:  ', list1)
print('Array: ', array1)

# 2D array
list2 = [[1, 2, 3], [4, 5, 6]]
array2 = np.array(list2)
print('List of lists:  ', list2)
print('Array of arrays:')
print(array2)


# 3D array
array3 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])


# Example 2: 
#Items in list may be of different types
list3 = ['name', 27, 4.0, True]
#Items in array must be of same type
array3 = np.array(list3)

print('List:  ', list3)
print('Array: ', array3)

# check data type within numpy array
print(array3.dtype)

# check each item at a time
for i in array3:
    print(type(i))


# Example 3: lenghts
#Same length
list4 = [[10, 20, 30], [40, 50, 60]]
array4 = np.array(list4)
print('list4 =  ', list4)
print('array4 = ')
print(array4)

#Different lengths 
list5 = [[10, 20, 30], [40, 50, 60, 70, 80]]
array5 = np.array(list5)
print('list5 =  ', list5)
print('array5 = ')
print(array5)
 
len(array5[0])
    

# Example 4: Slicing
list6 = [20, 40, 60, 80]
print('list6[:] = ', list6)
print('list6[1:] = ', list6[1:])
print('list6[:3] = ', list6[:3])
print('list6[2:4] = ', list6[1:4])
print('list6[-1] = ', list6[-1])
print('list6[-1:-3] = ', list6[-1:-3])
print('list6[-3:-1] = ', list6[-3:-1])

array6 = np.array(list6)
print('array6[:] = ', array6[:])
print('array6[1:] = ', array6[1:])
print('array6[:3] = ', array6[:3])
print('array6[2:4] = ', array6[2:4])
print('array6[-1] = ', array6[-1])
print('array6[-1:-3] = ', array6[-1:-3])
print('array6[-3:-1] = ', array6[-3:-1])


# Example 5: Items
list7 = [[20, 40, 60, 80], [10, 30, 50, 70]]
print(list7)
print('list7[0] = ', list7[0])
print('list7[0][:] = ', list7[0][:])
print('list7[0][1:] = ', list7[0][1:])
print('list7[0][:3] = ', list7[0][:3])
print('list7[0][2:4] = ', list7[0][2:4])
print('list7[0][-3:-1] = ', list7[0][-3:-1])

array7 = np.array(list7)
print(array7)
print('array7[0] = ', array7[0])
print('array7[0,:] = ', array7[0,:])
print('array7[0,1:] = ', array7[0,1:])
print('array7[0,:3] = ', array7[0,:3])
print('array7[0,-3:-1] = ', array7[0,-3:-1])

# Another example
list7 = [[20, 40, 60, 80], [10, 30, 50, 70]]
print(list7)
print('list7[:][0] = ', list7[:][0])
print('list7[1:][0] = ', list7[1:][0])
print('list7[:3][0] = ', list7[:3][0])
print('list7[0:2][0] = ', list7[0:2][0])
print('list7[-2:-1][0] = ', list7[-2:-1][0])

array7 = np.array(list7)
print(array7)
print('array7[:, 0] = ', array7[:, 0])
print('array7[1:, 0] = ', array7[1:, 0])
print('array7[:3, 0] = ', array7[:3, 0])
print('array7[-2:-1, 0] = ', array7[-2:-1, 0])


# Example 6: Conversion
list7 = [[20, 40, 60, 80], [10, 30, 50, 70]]
print(list7)
#list to array
array7 = np.array(list7)
print('array7: ', array7)
#array to list
list7 = array7.tolist()
print('list7: ', list7)


# Example 7: Special Arrays
#Special arrays
sarr1 = np.zeros(5)
print(sarr1)
sarr2 = np.zeros((2, 5))
print(sarr2)
sarr3 = np.ones(5)
print(sarr3)
#Array 0 to 1 (inclusive) with 3 points
sarr4 = np.linspace(0, 1, 6) 
print(sarr4)
# Array 10^1 to 10^2 (inclusive) with 3 points
sarr5 = np.logspace(1, 2, 3)
print(sarr5)

# difference with range()
sarr4b = list(range(1, 11))
print(sarr4b)



# Example 8: arange, shape, and reshape
#Shape and Reshape
#Use arange to generate array of 6 items 
arr = np.arange(6, dtype=int)
print(arr)
#Print array shape
print(arr.shape)

#Reshape to array 2 rows and 3 columns
arr2 = arr.reshape(2, 3)
print(arr)
print(arr.shape)


# Exampe 9: [:, None], flatten and ravel
list1 = [0, 1, 2, 3]
#Array 4 columns, 1 row
arr = np.array(list1)
print(arr)
print(arr.shape)
#Convert to array 1 column 4 rows
arr_col = arr[:, None]
print(arr_col)
print(arr_col.shape)
#Flatten to 1 row
arr_flt = arr_col.flatten()
print(arr_flt)
#Ravel: returns the view of the original array
arr_rvl = arr_col.ravel()
print(arr_rvl)
print(arr)


# Example 10: stack and transpose
#1d-arrays
a = np.array([2, 4, 6])
print(a)
b = np.array([1, 3, 5])
print(b)
#Stack ab
ab = np.stack((a, b))
print(ab)
#Transpose ab
ab = ab.T #or ab.transpose() 
print(ab)


# Example 11: Fancy indexing
list0 = [2, 4, 6, 8, 1, 5]
array0 = np.array(list0)
print('array0: ', array0)
array1 = array0[array0 > 4]
print('array0[array0 > 4]: ', array1)
array1 = array0[array0 < 4]
print('array0[array0 < 4]: ', array1)
array1 = array0[array0 != 4]
print('array0[array0 != 4]: ', array1)


# Example 12: Fancy indexing
list0 = [[2, 4, 6], [8, 1, 5]]
array0 = np.array(list0)
print('array0: ', array0)
array1 = array0[array0 > 4]
print('array0[array0 > 4]: ', array1)
array1 = array0[array0 < 4]
print('array0[array0 < 4]: ', array1)
array1 = array0[array0 != 4]
print('array0[array0 != 4]: ', array1)


# Example 13: NumPy Array and Vector Operations
v1 = np.array([5, 8]) #Vector 1
print('v1 = ', v1)
v2 = np.array([2, 4]) #Vector 2
print('v2 = ', v2)
v3 = v1 + v2
print('v1 + v2 = ', v3)
v4 = v1 - v2
print('v1 - v2 = ', v4)
v5 = v1 * 2
print('v1 * 2 = ', v5)
v6 = v1 * v2
print('v1 * v2 = ', v6)
v7 = v1 / v2
print('v1 / v2 = ', v7)
dist = np.sqrt(np.sum((v1 - v2) ** 2))
print('distance between v1 and v2: ', dist)


# Example 14: Maths and Stats
arrs = np.random.normal(size=(5, 2))    # size(rows, columns)
print('Array of 5 2D arrays: (random, mean: 0, std: 1)')
print(arrs)
print('mean = ', arrs.mean())
print('std = ', arrs.std())
print('minimum item = ', arrs.min())
print('index of minimum item = ', arrs.argmin())
print('sum = ', arrs.sum())
print('sum of columns = ', arrs.sum(axis=0))
print('sum of rows = ', arrs.sum(axis=1))
pos_values = (arrs > 0).sum() 
print('number of positive values = ', pos_values)

# if you want to make random numbers predictable you need to define a seed
# run both lines at all times, otherwise it won't work
np.random.seed(62) # define the seed
arrs = np.random.normal(size=(5,2))
print(arrs)



#*************** Matplotlib *****************
# Example 1: Basic plot – input y values
import numpy as np
import matplotlib.pyplot as plt

#Numbers on y-axis
y = [0, 1, 4, 9, 16]
#Pyplot will generate numbers x = [0, 1, 2, 3, 4] on x-axis
#Only need to plot y
plt.plot(y)
#Show the plot
plt.show()


# Example 2: Basic plot – input y values
import numpy as np
import matplotlib.pyplot as plt

#Numbers on y-axis
y = [0, 1, 0, 1, 0]
#Numbers on x-axis
x = [0, 1, 1, 2, 2] 

plt.plot(x, y)
plt.show()


# Example 3: Basic plot – input x and y from a function
import numpy as np
import matplotlib.pyplot as plt
#Spirograph
R = 5
k = 0.3 # try 0.3 and 0.1
l = 0.7  # try 0.7
x = []
y = []
for t in range(0, 1000):
    xx = R * ((1 - k) * np.cos(t) + l * k * np.cos((1-k)*t/k))
    x.append(xx)
    yy = R * ((1 - k) * np.sin(t) - l * k * np.sin((1-k)*t/k))
    y.append(yy)
#end spirograph

plt.plot(x, y)
#Show the plot
plt.show()


# Example 4: Display labels and title
import numpy as np
import matplotlib.pyplot as plt

# Generate 50 numbers between -10 and 10
x = np.linspace(-10, 10, 50)
# Parabola function
y = x**2
# Plot the function
plt.plot(x, y)
# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Parabola')
# Display it
plt.show()


# Example 5: Change plot style (default is -b for blue line)
# Generate 50 numbers between -10 and 10
x = np.linspace(-10, 10, 50)
# Parabola function
y = x**2
# Plot style 
plt.plot(x, y, 'o')  # test different styles: --, <, 1, p, *, D 
# Set labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Parabola')
# Display it
plt.show()


# Example 6: Multiple plots
# generate 0, 2, 4, 6, ..., 50
t = np.arange(0, 50, 2)
# data for first plot
x1 = t
y1 = t**0.5
s1 = '#ff7f0e' #red square
# data for second plot
x2 = t
y2 = t
s2 = 'b--' #blue dash
# data for third plot
x3 = t
y3 = t**1.5
s3 = 'g^' #green triangle
# plot all together
plt.plot(x1, y1, s1, x2, y2, s2, x3, y3, s3)
plt.show()


# Example 7: Color, line style, line width and legend
x = np.linspace(-10, 10, 50)

plt.plot(x, x**2, label='parabola', color='blue', 
         linestyle='--', linewidth=3)

plt.plot(x, x, label='straight line', color='red', 
         linestyle='-', linewidth=1)

plt.legend()
plt.show()


# Example 8: Scatter plot
import numpy as np
import matplotlib.pyplot as plt
N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2  # 0 to 15 point radii

plt.scatter(x, y, s=area, c=colors, alpha=0.5)
plt.xlabel('x')
plt.ylabel('y')
plt.show()



# another example:
import numpy as np
import matplotlib.pyplot as plt
N = 50
dict = {'a': np.arange(N),
        'b': np.random.randn(N),
        'c': np.random.randint(0, 20, N)}
dict['d'] = dict['a'] + 10 * np.random.randn(N)
dict['d'] = np.abs(dict['d']) * N

plt.scatter('a', 'b', c='c', s='d', data=dict)
plt.xlabel('a')
plt.ylabel('b')
plt.show()


# Example 8: Plotting with categorical variables
import numpy as np
import matplotlib.pyplot as plt
items = ['A1', 'A2', 'FE']
marks = [15, 10, 60]
plt.figure(figsize=(14, 4))  # in pixels

plt.subplot(132) #1 row, 3 columns, 1st col
plt.bar(items, marks)
plt.subplot(131) #2nd col
plt.scatter(items, marks)
plt.subplot(133) #3rd col
plt.plot(items, marks)
plt.suptitle('Categorical Plotting')
#plt.show()


# to save your plot as an image, put this before plt.show()
plt.savefig('example_plot.png', dpi=100)
plt.show()


# Example 9: Histogram
import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 100, 20
x = mu + sigma * np.random.randn(1000)

# the histogram of the data
plt.hist(x, 50, density=1, facecolor='b', alpha=0.7)

plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Histogram')
plt.text(60, .025, r'$\mu=100,\ \sigma=20$', fontsize = 12)  #adding text inside plot
plt.axis([20, 200, 0, 0.03]) 
plt.grid(True)
plt.show()


# to change the number of bins
bins_list = [40, 50, 60, 80, 110, 130, 180, 200]  # specify bin start and end points
plt.hist(x, bins = bins_list, density=1, facecolor='b', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Histogram')
plt.grid(True)
plt.show()

# to specify n bins
import math
w = 3  # create bins of size 3
n = math.ceil((x.max() - x.min())/w)   # x is our data
plt.hist(x, bins = n)
plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Histogram')
plt.grid(True)
plt.show()


# not sure if this is what Tanu meant
positions = (60, 80, 100, 140)
labels = ('a','b','c','d') # you can use numbers also
plt.xticks(positions, labels)

plt.hist(x, 50, density=1, facecolor='b', alpha=0.7)
plt.xlabel('Value')
plt.ylabel('Probability')
plt.title('Histogram')
plt.grid(True)
plt.show()

