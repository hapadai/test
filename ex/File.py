# -*- coding: euc-kr -*-

'''
Created on 2016. 11. 8.

@author: hapadai
'''

''' ���� open ''' 
''' read : ��ü �б� ''' 
f=open('newfile.txt', 'r')   
a=f.read()
print('read()'); print(a);print('\n')
f.close()

''' read() - 4byte �б� '''
h=open('newfile.txt','r')    
v=h.read(4)
print('read(4)'); print(v);print('\n')
h.close()

''' readline -  �����б� '''
g=open('newfile.txt', 'r')   
b=g.readline()
print('readline()'); print(b);print('\n')
g.close()

''' readlines() - ��ü �б� '''
e=open('newfile.txt','r')    
c=e.readlines()
print(c);print('\n')
e.close()

''' readline() - ���پ� �б� '''
f=open("newfile.txt", "r")
a=f.readline()
print('readline()'); print(a)
b=f.readline()
print(b);print('\n')
f.close

''' ���� ���� ��� ����ϱ�  '''
f=open('newfile.txt', 'r')
for line in f:
	print(line)
print('\n')
f.close()

''' ������ ���� ��� list �� ���� ''' 
f=open('txt/score.txt', 'r')
score=[]
for line in f:
	score.append(int(line))
print(score);print('\n')
f.close()

''' with open - ���� ��� list �� ���� ''' 
score2 = []
with open('txt/score.txt') as f:
	for line in f:
		score2.append(int(line))
print(score2);print('\n')
f.close()

''' ���� ���� ��� ������ �ֱ� ''' 
D={}
with open('txt/ban.txt', 'r') as f:
	for line in f:
		(key, val) = line.split()
		D[int(key)] = val
print()
print('save to dict')
for key, val in D.items():
	print(key, val)
print('\n')
f.close()

''' ���� ���� �߶� �ε������� ������ �ֱ� ''' 
S={}
with open('txt/student.txt', "r") as s:
	for line in s:
		stu = line.split()
		key = stu[0]
		values = stu[1:]
		S[key] = values
print('save to dict #2')
print(S)
s.close()
for key, values in S.items():
	print (key)
	for val in values:
		st = val.split()
		print(st)

''' ���� ����  '''
''' write - ���پ� ���� '''		
f = open('txt/subject.txt', 'w')
f.write('hello world')
f.write('python programming')
f.write('good bye')
f.close()		

''' writelines() - ������ ���� '''
f = open('subject2.txt', 'w')
f.writelines(['hello\n', 'world\n', 'python\n', 'program', 'good', 'bye'])
f.close()
