import numpy as np
s = np.array([
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9]
])

sum_column = s.sum(axis = 0)
sum_row = s.sum(axis = 1)
a = sum_column[sum_column == 45]
b = sum_row[sum_row == 45]
a1 = s[:3,:3]
a2 = s[3:6,:3]
a3 = s[6:9,:3]
a4 = s[:3,3:6]
a5 = s[3:6,3:6]
a6 = s[6:9,3:6]
a7 = s[:3,6:9]
a8 = s[3:6,6:9]
a9 = s[6:9,6:9] 
l = [a1.sum()==45,a2.sum()==45,a3.sum()==45,a4.sum()==45,a5.sum()==45,a6.sum()==45,a7.sum()==45,a8.sum()==45,a9.sum()==45,a.size == 9,b.size == 9]
if all(l):
    print("IT IS VALID SUDOKU")
else:
    print("IT IS NOT VALID SUDOKU")

