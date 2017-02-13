"""
1week - 12hour
12hour over - salary *1.3


input :
 1. work time for week
 2. salray for time

print :
 salary for week


sum = 0
overTime = 0
workTime = int(input("Input your work time for this week :"))
salaryForTime = int(input("Input your salary for time :"))

if workTime < 12 :
    sum = workTime * salaryForTime
else :
    overTime = workTime - 12
    sum = 12*salaryForTime + overTime*salaryForTime*1.3

print('Your total salary : %10d' %sum)



num = int(input('Input Integer : '))
print()

a=1
count=0
while a<=num:
    if num%a == 0:
        print(a)
        count +=1
    a += 1
print()
print(num, 'count :', count)

"""




               
