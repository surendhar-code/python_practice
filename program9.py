#grouping a elements in a list

def grouping(list1,n):
    for i in range(0,len(list1),n):
        yield list1[i:i+n]

list1=["suren","sai","aiyas","then","what","charan","ashwin","raja","smriti","davina"]
n=3
x=list(grouping(list1,n))
print(x)
    
