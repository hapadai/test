#range
for x in range(5):
    print(x)


for data in range(1,10,2):
    print(data+1)

for letter in 'PYTHON':
    print(letter)

for a in 'tony':
    y = a.upper()
    print(y)

#list
print('\nlist')
for x in [1,3,5,7,9]:
    print(x)

for x in [1,2,3,4,5]:
    for y in [2,4,6,8,10]:
        print('%3d' %(x*y), end=' ')
    print()

#dict
print('\ndict')
score={1:30, 4:20, 5:20, 3:20}
for x in score:
    print(x)

print('\ndict2')
for x in score.keys():
    print(x)

for x,y in score.items():
    print(x,y)

for x in score.values():
    print(x)

#dict
print('\nMath')
A=[x**2 for x in range(10)]
print(A)

B=[2**x for x in range(10)]
print(B)

C=[x for x in A if x%2==0]
print(C)
