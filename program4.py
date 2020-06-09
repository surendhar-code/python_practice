#reversing a list using reverse()
list1=[1,2,3,4]
print(list1)
list1.reverse()
print(list1)

help(list)

#reversing a list using slicing technique
def Reverse(list1):
    print(list1)
    newlist=list1[::-1]
    print(newlist)

list1=[1,2,3,4]
Reverse(list1)
