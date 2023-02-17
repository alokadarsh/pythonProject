num=[2,4,65,7,89,5,443,3,1,4,567,8]
smallest=num[-1]
second_smallest=num[-1]
third_smallest=num[-1]
for i in range(len(num)):
    if num[i]<smallest:
        smallest=num[i]
for i in range(len(num)):
    if num[i]<second_smallest and num[i]!=smallest:
        second_smallest=num[i]
for i in range(len(num)):
    if num[i]<third_smallest and num[i]!=smallest and num[i]!=second_smallest:
        third_smallest=num[i]

print(smallest,second_smallest,third_smallest)