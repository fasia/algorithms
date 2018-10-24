import random


def Partition(a, l, r):# input array a[l,r]
    p1=a[l]
    i=l+1
    #print('a,  range', a, range(l + 1, r))
    for j in range(l+1, r):
        if a[j] < p1:
     #       print('swaped')
            tmp = a[j]
            a[j] = a[i]
            a[i] = tmp
            i = i + 1
    t = a[l]
    a[l] = a[i-1]
    a[i-1] = t
    print("in partition", a)
    return a


def QuickSort(a ,n):
    if  n==1 or n==0:
        return
    piv = a[0]
    #partition a around p
    Partition(a,a.index(piv) ,n)
    p=a.index(piv)
    leftPart=[]
    rightPart=[]
    #print('partitioned array', a, 'p', p)
    print('qsl', a[:p],'lenght', len(a[:p]), 'qsr',a[p+1:],'lenght',len(a[p+1:]) )
    #print('count after qsl',)
    leftPart=QuickSort(a[:p],len(a[:p])) #recursive sort the first part
    print('leftpart', leftPart)
    #print('count after qsr',end-p)
    #print('qsr',a[p:], p+1, end)
    rightPart=QuickSort(a[p+1:], len(a[p+1:])) #recursive sort 2nd part

    return



array=[3, 8, 2, 5, 1, 4, 7, 6]
count=0
#print(a[:1], a[1:] ,a[-1:])

sortedArray=QuickSort(array,len(array))
print(sortedArray)

# def quickSort(alist):
#    (alist,0,len(alist)-1)
#
# def quickSortHelper(alist,first,last):
#    if first<last:
#
#        splitpoint = partition(alist,first,last)
#
#        quickSortHelper(alist,first,splitpoint-1)
#        quickSortHelper(alist,splitpoint+1,last)
#
#
# def partition(alist,first,last):
#    pivotvalue = alist[first]
#
#    leftmark = first+1
#    rightmark = last
#
#    done = False
#    while not done:
#
#        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
#            leftmark = leftmark + 1
#
#        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
#            rightmark = rightmark -1
#
#        if rightmark < leftmark:
#            done = True
#        else:
#            temp = alist[leftmark]
#            alist[leftmark] = alist[rightmark]
#            alist[rightmark] = temp
#
#    temp = alist[first]
#    alist[first] = alist[rightmark]
#    alist[rightmark] = temp
#
#
#    return rightmark

#alist = [3, 8, 2, 5, 1, 4, 7, 6]

#array= [3, 8, 2, 5, 1, 4, 7, 6]

#QuickSort(array, len(array))
#print(array)




def swap_values(lst, val1, val2):
    lst[val1], lst[val2] = lst[val2], lst[val1]

def quicksort(array, start, end):

    if start < end:

        partition_index = partition(array, start, end) #
        quicksort(array, start, partition_index - 1)
        quicksort(array, partition_index + 1, end)

def partition(array, start, end):

    pivot = end
    partition_index = start

    for i in range(start, end):

        if array[i] < array[pivot]:
            print("{} is less than {}".format(array[i], array[pivot]))
            swap_values(array, partition_index, i)
            partition_index += 1

    array[pivot], array[partition_index] = array[partition_index], array[pivot]
    return partition_index


# ...
def partition(array, start, end):
    if start < end:
        pivot = random.randint(start, end)
        array[end], array[pivot] = array[pivot], array[end]
        partition_index(array, start, end)

