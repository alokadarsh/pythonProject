s=input("enter string")
i=0
s1=""
for x in s:
    if s.index(x)==i:
        s1=s1+x
    i=i+1
print(s1)
