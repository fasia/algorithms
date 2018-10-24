

count = 0
def Partition(a, l, r):# input array a[l,r]
    p1=a[l]
    i=l+1
    for j in range(l+1, r):
        if a[j] < p1:
            tmp = a[j]
            a[j] = a[i]
            a[i] = tmp
            i = i + 1
    t = a[l]
    a[l] = a[i-1]
    a[i-1] = t


def QuickSort(a,start ,end):
    if  end-start==0 :
        return

    #count the number of comparisions. (lenghtof Array-1)
    global count
    count += end-start-1

    piv = a[start]
    Partition(a, start, end)
    p=a.index(piv)

    QuickSort(a, start,p) #recursive sort the first part
    QuickSort(a, p+1,end) #recursive sort 2nd part



def QuickSortLastElement(a,start ,end):
    if  len(a[start:end]) <=1:
        return

    global count
    count += end-start-1
    piv = a[end-1]

    #swap with first element
    m = a.index(piv)
    temp = a[start]
    a[start] = a[m]
    a[m] = temp

    #partition the array
    Partition(a, start, end)

    # find the index of pivot
    p=a.index(piv)

    QuickSortLastElement(a, start,p) #recursive sort the first part
    QuickSortLastElement(a, p+1,end) #recursive sort 2nd part


def QuickSortMedianElement(a,start ,end):
    if  len(a[start:end])<=1 :
        return
    #find the median
    lengthofArray = len(a[start:end])
    if lengthofArray%2 ==0 : # even number
        median = (lengthofArray/2)-1
    else:
        median = lengthofArray/2
    # assign values of first, last and median
    a_a=[]
    a_a=a[start:end]
    c = a_a[median]
    bb= a[end-1]
    aa= a[start]

    # find median
    piv = findMedian(aa,bb,c)

    #swap the location of pivot with the first location
    m=a.index(piv)
    temp= a[start]
    a[start]= a[m]
    a[m]=temp

    global count
    count += end-start-1
    Partition(a, start, end)

    p=a.index(piv)
    QuickSortMedianElement(a, start,p) #recursive sort the first part
    QuickSortMedianElement(a, p+1,end) #recursive sort 2nd part


def findMedian(a,b,c):
    if a > Bigger(b,c):
        return Bigger(b,c)
    elif a < Smaller(b,c):
        return Smaller(b,c)
    else:
        return a


def Bigger(i,j):
    if i>j:
        return i
    else:
        return j

def Smaller(i,j):
    if i<j:
        return i
    else:
        return j

#---------------------------------
#answer for qs1_20.txt = 91
#                        78
#                        66
#answer for qs2_20.txt =69
#                       65
#                       56
#
#answer for qs1_100000 =2127173
#                       2079088
#                       1749103
#----------------------------------



f = open("QS_10000.txt", 'r')
array=[]
array2=[]
array3=[]
for i in range(0, 10000):
    l=f.readline().strip()
    if l!= '':
        array.append(int(l))
        array2.append(int(l))
        array3.append((int(l)))

QuickSort(array,0,len(array2)) # AMSWER: 162085
print(count)

count=0
QuickSortLastElement(array2,0,len(array2)) #last element is pivot 164123
print(count)

count=0
QuickSortMedianElement(array3,0,len(array3)) #last element is pivot 138382
print(count)


