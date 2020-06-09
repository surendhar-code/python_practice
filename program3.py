
#element exist in list or not

list1=[1,2,3,4,5]
existele=3
count=0
for i in list1:
    if i == existele:
        count+=1
if count==0:
    print("The element {0} is not exist in the list".format(existele))
else:
    print("The element {0} is exist in the list".format(existele))


        
