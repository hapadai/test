'''
Created on 2016. 10. 28.

@author: hapadai
'''

if __name__ == '__main__':

	
	a = int(input('Enter a : ')) 
	b = int(input('Enter b : '))
	
	try:
		c=a/b
		print(c)
	except ZeroDivisionError:
		result = 'Cannot divid by 0'
	else:
		result = 'OK'
	finally:
		print(result)
		