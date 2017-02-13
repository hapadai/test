# -*- coding: euc-kr -*-

'''
Created on 2016. 11. 8.

@author: hapadai
'''

''' 파일 open ''' 
''' read : 전체 읽기 ''' 
f=open('newfile.txt', 'r')   
a=f.read()
print('read()'); print(a);print('\n')
f.close()

''' read() - 4byte 읽기 '''
h=open('newfile.txt','r')    
v=h.read(4)
print('read(4)'); print(v);print('\n')
h.close()

''' readline -  한줄읽기 '''
g=open('newfile.txt', 'r')   
b=g.readline()
print('readline()'); print(b);print('\n')
g.close()

''' readlines() - 전체 읽기 '''
e=open('newfile.txt','r')    
c=e.readlines()
print(c);print('\n')
e.close()

''' readline() - 한줄씩 읽기 '''
f=open("newfile.txt", "r")
a=f.readline()
print('readline()'); print(a)
b=f.readline()
print(b);print('\n')
f.close

''' 파일 내용 모두 출력하기  '''
f=open('newfile.txt', 'r')
for line in f:
	print(line)
print('\n')
f.close()

''' 파일의 내용 모두 list 에 저장 ''' 
f=open('txt/score.txt', 'r')
score=[]
for line in f:
	score.append(int(line))
print(score);print('\n')
f.close()

''' with open - 파일 모두 list 에 저장 ''' 
score2 = []
with open('txt/score.txt') as f:
	for line in f:
		score2.append(int(line))
print(score2);print('\n')
f.close()

''' 파일 내용 모두 사전에 넣기 ''' 
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

''' 파일 내용 잘라서 인덱스별로 사전에 넣기 ''' 
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

''' 파일 저장  '''
''' write - 한줄씩 저장 '''		
f = open('txt/subject.txt', 'w')
f.write('hello world')
f.write('python programming')
f.write('good bye')
f.close()		

''' writelines() - 여러줄 쓰기 '''
f = open('subject2.txt', 'w')
f.writelines(['hello\n', 'world\n', 'python\n', 'program', 'good', 'bye'])
f.close()
