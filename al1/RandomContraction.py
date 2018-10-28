#The file contains the adjacency list representation of a simple undirected graph. There are 200 vertices labeled 1 to
#  200. The first column in the file represents the vertex label, and the particular row (other entries except the first
#  column) tells all the vertices that the vertex is adjacent to. So for example, the 6^{th}6th row looks like :
# "6	155	56	52	120	......". This just means that the vertex with label 6 is adjacent to (i.e., shares an edge with)
#  the vertices with labels 155,56,52,120,......,etc

#Your task is to code up and run the randomized contraction algorithm for the min cut problem and use it on the above
#  graph to compute the min cut. (HINT: Note that you'll have to figure out an implementation of edge contractions.
# Initially, you might want to do this naively, creating a new graph from the old every time there's an edge
# contraction. But you should also think about more efficient implementations.) (WARNING: As per the video lectures,
# please make sure to run the algorithm many times with different random seeds, and remember the smallest cut that you
# ever find.)

import random
import copy
from random import seed
from random import sample





def randomContraction(a):
    #while the number of nodes is more than 2
    #pick a remaining edge (u,v) uniformly at random
    #merge  u and v into a single vertex
    #remove self-loops
    #return cut represented by final 2 vertices.
    #print('array is', a)
    #generate some numbers
    sequence = a[:]
    while (len(sequence)>2):
        node1= random.choice(sequence)
        vertex = int(random.choice(node1[1:]))
        while vertex == node1[0]:
            vertex = int(random.choice(node1[1:]))
        #print('sequence', sequence)
        node2 = findNode2(sequence,vertex)
        #print('node1, node2, and their vertex', node1, node2, vertex)
        old = node1[0]
        #print('node1: ', node1, 'node2: ', node2)

        # Merge node1 and node2 and delete the loops (if there is any)
        newNode= mergeVertices(node2,node1)
        #print('contracted together into a new node:', newNode)

        # remove the two selected nodes and add the merged node
        sequence.remove(node1)
        sequence.remove(node2)
        sequence.append(newNode)
        #print('old node', old, 'new node', vertex)

        # Change name of the merged node into superNode throughout the whole array
        sequence = renameArrayWithNewNode(sequence, old,vertex)
        #print('sequence after a contraction', sequence)
        #print('--------------------')
    return len(sequence[0])-1




def findNode2(s,v):
    for i in s:
        if int(i[0]) == v:
            return i


def mergeVertices(m, n):
    mergedNode = []
    #mergedNode.append(m[0])
    for i in m:
        if i != n[0]:
            mergedNode.append(i)
    for j in n:
        if j!= m[0] and j!= n[0]:
            mergedNode.append(j)
    #print('merge is', mergedNode)
    return mergedNode


def renameArrayWithNewNode(s, old, new):
    for i in range(len(s)):
        for j in range(len(s[i])):
            if int(s[i][j]) == int(old):
                s[i][j]=int(new)
    return s


f = open("KargerMinCut.txt", 'r')
array = []
for i in range(0, 200):
    l= f.readline().strip()
    if l != '':
        array.append(l.split('\t'))

for i in range(len(array)):
    for j in range(len(array[i])):
        array[i][j]= int(array[i][j])
copyArray = copy.deepcopy(array)
#copyArray = [[array[x][y] for y in range(len(array[0]))] for x in range(len(array))]
mincut = randomContraction(copyArray)

#print(' first mincut', mincut)
print('+++++++++++++++++++++')
copyArray = copy.deepcopy(array)
#print('coppppp', copyArray)
for c in range(500):
    copyArray = copy.deepcopy(array)
    newcut = randomContraction(copyArray)
    #print('mincut calculated:',newcut)
    #print('==========================')
    if newcut < mincut:
        mincut = newcut
        print(' new mincut', mincut)

print('mincut:', mincut)
