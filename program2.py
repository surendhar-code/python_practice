#swap two numbers in a list

def swap(list1):
    print("before swapping:",list1)
    temp=list1[0]
    list1[0]=list1[1]
    list1[1]=temp
    print("after swapping:",list1)

list1=[2,3]
swap(list1)
