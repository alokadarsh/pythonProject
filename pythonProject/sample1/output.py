l1=[1,2,3,4,5]
l2=[]
for i in range(len(l1)):
    if (l1[i]%2)==0:
        continue
    l2.append(l1[i])
print(l2)