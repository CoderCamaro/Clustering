'''
Clustering 1d data into 2 groups.

Algorithm
1. Make a list of numbers (X)
2. Create empty list to hold labels of each data point (y)
3. Find mid way point between highest number of X and lowest number of X
4. Label numbers less and equal than mid way point 0 
5. Label numbers that are higher than the mid way point 1

Date Started : 11/16/23
Date Ended : 12/14/23
Total Hours to Complete : 4 hours
'''

X = [1,8,2,9] # Input
y = [] # Output (Labels of data)


Mid = ((max(X)-min(X)) / 2) + min(X)

for i in X :
    if i <= Mid:
        y.append(0)
    else:
        y.append(1)

print(y)