# Faezeh Siavashi
# November 2nd 2018

import sys, threading

sys.setrecursionlimit(800000)
threading.stack_size(67108864)
import time
from collections import Counter, defaultdict



def main():
    timerstart = time.time()
    t0 = time.time()
    g, grev = read_file()  # graph g with its reverse grev
    t1 = time.time()
    print 'file is read, the timer is ', t1-t0

    a = []
    for n in xrange(1,875715): #number of Nodes+1
        a.append(n)
    global leader
    leader = dict.fromkeys(a, 0)  # create a leader dictionary for all nodes 'nodeID': 'leaderID'
    global exploredNodes
    exploredNodes = dict.fromkeys(a,0)

    # global ftStack
    # ftStack = []
    global ft
    ft =[]

    t2 = time.time()
    #compute "magical ordering" of nodes
    dfs_loop(grev, True)
    t3= time.time()

    print 'timer after first loop is:', t3-t2

    global mystack
    mystack = ft[:]

    exploredNodes.clear()
    exploredNodes = dict.fromkeys(a,0)

    # discover the SCCs one-by-one
    t4 = time.time()
    dfs_loop(g, False)
    t5 = time.time()
    print 'timer after second loop is:', t5-t4

    timerStop = time.time()
    print 'Total timer time is:', timerStop-timerstart
    maxx= Counter(leader.values()).most_common()[:5]

    print 'counter', maxx

#     with open("SCC_input3200.txt") as f:  ANSWER is 2738,240,140,42,36, For SET time is , 0.0667781829834, was 3.55507898331
#  and 0.290647983551

# with SCC_input20000, ANSWER is 12634,6703, 253, 113, 139 in TIME is changed to 0.560821056366,  35.49 sec form 94.89
# which was 259.906612158!

# with SCC_input80000 , answer is {1: 49989, 49990: 22871, 72856: 3431, 77099: 2105, 76288: 822 Time 3.01637 ,1555.5sec, 1417.1 sec
# with SCC_L , 875714 nodes ANSWER is (434821,968,459,313,211), TIME 60.38 SEC

def read_file():
    array = []
    rev_array = []

    with open("SCC_L.txt") as f:
        for l in f:
            array.append(l.rstrip('\n').split())
    for i in xrange(len(array)):
        for j in range(len(array[i])):
            array[i][j] = int(array[i][j])
        rev_array.append(list(reversed(array[i])))

    # make a dictionary of the list and its reverse
    a = makeDictionary(array)
    b = makeDictionary(rev_array)
    return a,b

def makeDictionary(g):

    d= defaultdict()
    for i in g:
        d.setdefault(i[0], []).append(i[1])
    return d




def dfs_loop(graph, rev):
    global t # for finishing times in the first pass
    t = 0

    global s # for leaders in the second pass
    s= 0

    global exploredNodes
    c =0
    global mystack
    if rev:
        for i in xrange(875714,0,-1): # loop over the nodes
            if exploredNodes[i]==0:
                s =i
                dfs(graph,i)
    else:
        while len(mystack)!= 0:
            i = mystack.pop()
            if exploredNodes[i]==0:
                s =i
                dfs(graph,i)



def dfs(g, i):
    #mark i as explored
    global exploredNodes
    exploredNodes[i]=1

    # set the leader
    global s
    global leader
    leader[i] = s

    # go until the end of the graph with node i
    if g.get(i) != None:
        for h in g.get(i):
            if exploredNodes[h]==0:
                dfs(g, h)
    global t
    t +=1
    global ft
    ft.append(i)




thread = threading.Thread(target=main)
thread.start()