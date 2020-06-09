#Finding the cumulative sum oof the elements in the list

def cumsum(list1):
    print(list1)
    list2=[]
    cu=0
    n=len(list1)
    for i in range(0,n):
        cu+=list1[i]
        list2.append(cu)
    print(list2)

list1=list(range(1,10))
cumsum(list1)
