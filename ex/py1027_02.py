
#test1
'''
def cacl(time, sal):
    total = time * sal
    print(total)
    if time>12 :
        re = time-12
        add = re*sal*0.3
        print(add)
        total += add
    return total

#main
t = int(input('time :'))
s = int(input('sal : '))
to = cacl(t,s)
print('total salary : %.2f' %to)

'''

#test2
'''
def ch(aa):
    return aa*9/5+32


s=int(input('start :'))
e=int(input('end :'))

for i in range(s,e+1,1):
    print ('aaa', i, 'is', ch(i))
'''

#test3
import random
ram = random.randint(1,100)
innum = 0
count=0
print(ram)

while(ram != innum):
    innum = int(input('input:'))
    if ram > innum :
        print ('big')
    else :
        print ('small')
    count+=1
print (count, innum)
        
        

