# Test1

kor = int(input('KOR Score :'))
math = int(input('Math Score :'))
eng = int(input('Eng Score :'))

print()
print('Input Score')
print('-----------')  #print('-' * 10)
print('KOR Score :', kor)
print('Math Score :', math)
print('Eng Score :', eng)
print()

total = kor + math + eng
avg = total/3

print('Total Score :', total)
print('Average :%.2f' %(avg))
