""""
                University of Canberra
        Programming for Data Science G (11521) - 2022 (S2)
                    Assignment 3

Question 3 [4 marks] (Error): There is a logical error in the function implementation below and the program only
outputs the following [(-0.379504, -0.725536)] instead of all data in the ellipse2a.txt file. Use this ellipse2a.txt
file in Week 4 Tutorial.

Correct the function implementation and run the program to output all data from the file as follows
[(0.810831, -0.552096), (1.357364, 1.165427), (0.464588, 0.34218), (-0.643902, 0.164353), (0.836779, 0.896883),
 (-1.486807, -0.659875), (-1.08032, -0.691931), (-0.454588, - 1.313122), (0.015564, 0.301778), (0.505334, -0.808687),
(-0.04276, 1.120155), (-1.208152, 0.058249), (0.703988, -0.228097), (-1.15505, -0.714617), (-0.534014, 0.581944),
         . . . . . . # some lines deleted to reduce length
(3.358179, 1.207931), (4.333138, 1.123023), (4.500865, 2.093882), (4.174701, 4.928042),
(3.140143, 2.522568), (4.281658, 3.494965), (3.551645, 1.458362), (4.178576, 4.075363),
(4.237745, 3.754904)]

FAQs:
1. Is there a partial marking if I could read and output only few data points, instead of all the data
in the ellipse2a.txt?
No. There will be NO partial marking.

Marking rubric:
    
Fixing the error- 4 Marks
"""

def read_ellipse_file(filename):
    dataset = []
    f = None
    try:
        f = open(filename, 'r')
        while True:
            line = f.readline()
            if len(line) == 0: #end of file
                break
            line = line.replace('\n', '')
            xystring = line.split(' ')
        dataset.append((float(xystring[0]), float(xystring[1])))
    except Exception as ex:
        print(ex.args)
    finally:
        if f:
            f.close()
    return dataset
#end of function

data = read_ellipse_file('Files4A3/ellipse2a.txt')
print(data)
