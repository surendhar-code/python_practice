#python program to interchange first and last elements in a list.

def firstlast(list1,n):
    beg=list1[0]
    end=list1[n]
    print("The first and last element of the list {0} is {1} and {2}\n".format(list1,beg,end))


list1=list(range(0,5))
print(list1)
n=(len(list1))-1
firstlast(list1,n)
