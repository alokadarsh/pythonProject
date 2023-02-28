p="alokadarsh @ihi hello ok"
l=[]
k=[]
l.extend(p)
for i in l:
    if i==" " or i=="@":
        continue
    else:
        k.append(i)
print(k)
r=''.join(k)
print(r)