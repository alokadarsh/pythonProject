print("test case1")
a=6
b=8
def test():
    sum=a+b
    print(sum)
test()

print("test case 2")
def test2(a,b):
    sum=a+b
    sub=a-b
    print(sum,sub)
test2(68,98)
print("test case 3")
def test3(a=14,b=9):
    sum=a+b
    sub=a-b
    print(sum,sub)
test3()

print("test case 4")
def test4(a=14, b=98):
    sum = a + b
    sub = a - b
    print(sum, sub)

test4()
test4(87,65)
print("test case 5")
a=6
b=8
def test(a=6,b=4):
    sum=a+b
    print(sum)

test(5,6)
test()
test()
test2(4555,6)
