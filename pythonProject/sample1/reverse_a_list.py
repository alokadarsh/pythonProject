list1=[2,4.5,56,'r','rtrt',4]
list2=[]
for i in range(1,len(list1)+1):
    list2.append(list1[-i])
print(list2)