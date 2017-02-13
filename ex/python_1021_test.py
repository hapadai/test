#test1
#for, range
for x in range(10):
    print(x, end =' ')

print()

for x in range(10):
    print(x*5, end =' ')

print()

for x in range(10,0,-1):
    print(x, end =' ')
print()
    
#test2
"""    
score=[]
for x in range(5):
    num = int(input('Input score :'))
    score.append(num)

print()
print('Input score : ', score)
print('Max Score :', max(score))
print('Min Score :', min(score))

avg = sum(score)/len(score)
print('Average : %.2f' %avg)
print()
"""

score = {1:[80,90,86], 2:[78,88,85], 3:[85,85,92], 4:[70,69,65], 5:[90,95,100]}
for x,y in score.items():
    avg = sum(y)/3
    print('%d order : %f' %(x,avg))
