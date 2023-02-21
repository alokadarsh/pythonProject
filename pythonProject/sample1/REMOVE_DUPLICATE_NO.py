n=int(input("enter length of string"))
l1=[]
for i in range(n):
    element=int(input("enter list value"))
    l1.append(element)
result=[]
for i in l1:
    if i not in result:
        result.append(i)
print(result)


