"""
def find_max(a,b):
    if a>b :
        y=a
    else :
        y=b
    return y

#main
m=find_max(1,3)
n=find_max(4,1)
print(m,n)


def hello():
    print('hello world!!')
    print('Hello python~')

hello()
print('111')
hello()
print('222')


def calculate(k, e, m):
    total = k+e+m
    ave = total/3
    return ave

#main
'''
k=int(input('input k :'))
e=int(input('e:'))
m=int(input('m :'))
avg = calculate(k,e,m)
print(avg)
'''

'''
def sum_mult(a,b):
    sum1=a+b
    mult=a*b
    return sum1, mult

#main
k=int(input('a:'))
e=int(input('b:'))
m,n=sum_mult(k,e)
print(m,n)

'''
"""
'''
def test():
    b=20
    print(a,b)

#main
a=100
print(a)
test()
#print(b)
'''

'''
def fun1():
    a=100
    b=200
    print(a,b)

#main
a=300
print(a)
#print(b)
fun1()

'''

def test(M):
  M[2] += 2
  M[4] += 10
# main
L = [90,80,95,85,77,83]
test(L)
print(L)



def inc(a,step=1):
    return a+step

b=inc(10)
print(b) # 11

c=inc(10,50)
print(c) #60


def f(a=1):
    print(a)

f()



def ff(*nam):
    for n in nam:
        print(n.title())

f('aaa','bbb','ccc')
print('-------')
f('ddd', 'eee', 'fff')


def name_age(**lists):
    print(lists)

name_age(aa=10, bb=20)
print('------')
name_age(cc=30, ddd=40)




def add(x,y):
    return x+y

lambda x,y:x+y


def fs(x):
    return x*x

x=[1,2,3,4,5]
L=list(map(f,x))
print(L)



y=[3,4,5]
L1=list(map(lambda x:x*x, y))
print(L1)

L2=list(map(lambda x:x*x+4*x+5, range(10)))
print(L2)


import math
math.pow(2,3)

