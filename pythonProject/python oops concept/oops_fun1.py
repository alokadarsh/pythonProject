a=6
b=8
def test():
    sum=a+b
    print(sum)
test()


def test2(a,b):
    sum=a+b
    sub=a-b
    print(sum,sub)
test2(68,98)

def test3(a=14,b=9):
    sum=a+b
    sub=a-b
    print(sum,sub)
test3()


def test4(a=14, b=98):
    sum = a + b
    sub = a - b
    print(sum, sub)


test4()
test4(87,65)
