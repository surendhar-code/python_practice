#finding a duplicate elements in a list

def duplicate(list1):
    n=len(list1)
    repeated=[]
    for i in list1:
        k=i+1
        for j in range(k,n):
            if list1[i]==list1[j] and list1[i] not in repeated:
                repeated.append(list1[i])
    print(repeated)

list1=[10,20,12,13,14,14,14,6,7,8,9,9,9]

duplicate(list1)
