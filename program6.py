#removing multiple elements in a list
#method-1 using a remove()
list1=list(range(1,20))
print(list1)
# here we remove the elements which is divisible by 2
for i in list1:
    if i%2==0:
        list1.remove(i)
print(list1)

#removing elements using slicing
list1=list(range(1,20))
print(list1)
del(list1[:10]) #deleting the elements from the list in the range of 1:10


print(list1)

#Removing a empty tuples in a given list

def removetuples(list1):
    list1=filter(None,list1)
    print(list1)

tuples=[(),(1,2,3,4),(","),("suren","sai"),(),("ooviya","sumaiya"),(),()]
removetuples(tuples)
