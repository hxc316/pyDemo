import time


# for i in range(10):
    # print(i)

# print(time.strftime('%M',time.localtime(time.time())))


def a1():
    a=['a','b']
    while a:
        print(a.pop())

# a1()


def a2():
    a = [1,2,3,4,5,6];
    b = [];
    for a1 in a:
        if a1 < 4:
            b.append(a1)
    print(b)

# a2()

def p1(name):
    print(name.title())

# p1("aa is good")

def p2(name,name2="hi"):
    print("name:",name)
    print("name2:",name2)

# p2("hu","123")


def f1(*m):
    print(m[0])

# f1("a","b")

def f2(a,**m):
    print("a=",a)
    for key,vlue in m.items():
        print(key)
    print(m['a2'])

f2("a",a1="1",a2="2")




