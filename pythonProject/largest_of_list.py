num=[2,4,65,7,89,5,443,3,4,567,8]
largest=num[0]
second_largest=num[0]
third_largest=num[0]
for i in range(len(num)):
    if num[i]>largest:
        largest=num[i]
for i in range(len(num)):
    if num[i]>second_largest and num[i]!=largest:
        second_largest=num[i]
for i in range(len(num)):
    if num[i]>third_largest and num[i]!=largest and num[i]!=second_largest:
        third_largest=num[i]

print(largest,second_largest,third_largest)