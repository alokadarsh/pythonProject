s1="I need to remove all vowels from this string"
s2="aeiouI"
s3=""
for i in s1:
    if i in s2:
        continue
    s3=s3+i

print(s3)