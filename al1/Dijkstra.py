#Faezeh Siavashi
#Nov 9th 2018


# Dijkstra's algorithm: finding shortest paths from the given node to all other nodes


def DijkstraShortestPath(e):
    x = []
    x.append(1)
    # set the array of shortest lengths for each node from Node1
    g=[]
    for i in xrange(1,201):# number of graph nodes = 200
        g.append(i)
    a= dict.fromkeys(g,0)
    i =1
    while len(x)<=200:
        miniLength = 1000000  # set the shortest distance to infinity
        nextNode = 0  # set the next node to null

        for connectedNodes in e:
            if connectedNodes[0] in x : # the source of the edge is visited
                for n in connectedNodes[1:]:
                    if n[0] not in x:
                        # choose the minimum length
                        if miniLength > a[connectedNodes[0]] + n[1]:
                            miniLength = a[connectedNodes[0]] + n[1]
                            nextNode = n[0]
        print 'The next node is', nextNode, 'with the length', miniLength
        #add next node to the visited nodes (x)
        x.append(nextNode)

        # set the new shortest length
        a[nextNode] = miniLength
        i+=1
    print('x', x)
    print('a',a)
    s=[7,37,59,82,99,115,133,165,188,197] # prints shortest paths for these selected nodes
    for k in s:
        print(a[k]),





def readfile_dict(): # reading a file and make a dictionary
    e = dict()

    with open("DijkstraData.txt") as f:
        for l in iter(f.readline,''):
            got= l.strip('\n').split('\t')
            e[int(got[0])] =0
            temp=[]
            for g in got[1:]:
                temp.append(map(int, g.split(',')))
            e[int(got[0])] = temp

    print 'e', e[4][0][0]
    return e

def readfile():
    e= []
    with open("DijkstraData.txt") as f:
        for l in iter(f.readline, ''):
            got = l.strip('\n').split('\t')
            temp =[]
            temp.append(int(got[0]))
            for i in got[1:]:
                temp.append(map(int,i.split(',')))
            e.append(temp)
    print('e', e, len(e[0]))
    return e

e = readfile()

DijkstraShortestPath(e)



