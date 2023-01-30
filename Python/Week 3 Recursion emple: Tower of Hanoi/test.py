""" import numpy as np

# create NumPy array
some_array = np.array([[1, 1, 2], [3, 3, 7], [4, 3, 1], [9, 9, 5], [6, 7, 7]])
print('original\n',some_array)

# swap rows 1 and 4
some_array[[0, 3],[0,0]] = some_array[[3, 0],[0,0]]

# view updated NumPy array
print('swapped:\n',some_array) """


z = ["alpha", "bravo", "charlie"]
new_z = [i[0]*2for i in z]
print(new_z)
