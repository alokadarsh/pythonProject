l1=[4,3,5,2,5,6,2,4,5,24]
for i in range(0,len(l1)):
    for j in range (i+1,len(l1)):
        if l1[i]>=l1[j]:
            l1[i],l1[j]=l1[j],l1[i]
print(l1)