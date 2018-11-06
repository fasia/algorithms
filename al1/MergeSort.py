# Programming assignment 2
#30 Sep 2018

# counting number of inversions in a given file

import os, sys

def Sort_and_Count(a):
    if len(a)==1:
        return a, 0
    else:
        B = a[:len(a)/2] # first half of array
        C = a[len(a)/2:] # second half of array

        B, X = Sort_and_Count(B)
        C, Y = Sort_and_Count(C)

        i = 0
        j = 0
        z = X+Y

        D = []
        # merge sort and count the inversions
        while i < len(B) and j < len(C):
            if int(B[i]) <= int(C[j]):
                D.append(B[i])
                i = i + 1
            else:
                D.append(C[j])
                j = j + 1
                z = z + (len(B) - i)
        D += B[i:]
        D += C[j:]
    return D, z







f = open("inv_assignment.txt", 'r')
array=[]
for i in range(0, 100000):
    array.append(f.readline().strip())

a, count= Sort_and_Count(array)
print(count)
