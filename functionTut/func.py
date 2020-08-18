y = '9'
print(type(y))
y = int(y)

print(type(y))


def exp(arg1, arg2, *argN):
    print(arg1)
    print(arg2)
    for arg in argN:
        print(arg,end =' ')

exp(1,2,3,4,5,6,7,8,9)


# sum = lambda a1, a2, a3: a1+a2+a3;

# print(sum(10,20,30))

def factorial(n):
    return 1 if n<2 else n *  factorial(n-1)

print(factorial(5))
print(type(factorial))

print(factorial.__doc__)
print(factorial.__name__)

import math;

def isPrime(no):
    flag = True
    for i in range(2, math.ceil(n//2)+1, 1):
        if(n % i == 0):
            flag = False
            break
    return flag
# n = int(input('no n'))
# print('{} is Prime'.format(n)) if(isPrime(n)) else print('{} is not a Prime'.format(n))

import time

ticks = time.time()
print("number {}".format(ticks))

localtime = time.localtime(time.time())
print(localtime)
print(localtime.tm_mon)
localtime = time.asctime(time.localtime(time.time()))
print(localtime)
# print(localtime)


import calendar
cal = calendar.month(2020,9)
print(cal)

print(calendar.calendar(2020, w=4, l=1, c=6))

print(calendar.firstweekday())
print(calendar.isleap(2020))
print(calendar.leapdays(2020, 2025))
print(calendar.month(2020,8, w=4, l=1))

import os;
print(os.getcwd())
print(os.path.join('E:\python workspace\functionTut','py1.doc'))
print(os.path.expanduser('~'))
pathname ='E:\\python workspace\\functionTut'
print(os.path.split(pathname))
import glob
print(glob.glob("*.py"))
import time
metadata = os.stat('func.py')
print(time.ctime(metadata.st_mtime))
print(metadata.st_size)
print(os.path.realpath("tree.py"))
# os.rename('ex.py','ee.py')
# os.remove('ee.py')
# os.mkdir('test')
# os.rmdir('test')
# os.chdir('test')
'''
fo = open("filename.txt","r+")
fo.write("swathi acharya")
print(fo.closed)
print(fo.mode)
print(fo.name)
# print(fo.softspace)
string = fo.readline(1)
pos = fo.tell()
print(pos)
print(string)
fo.close()
'''
'''
import shelve
shelfFile = shelve.open('mydata')
cats = ['bella','tiger']
shelfFile['cats'] = cats
shelfFile.close()

# import sys

# import sys

# if(len(sys.argv) < 2):
#     print('please provide')
#     sys.exit()
# print('there are %d argument' %len(sys.argv))

try:
    fh = open('mice.txt','r')
    print('try')
    fh.write('ss')
    fh.close()
except Exception as err:
    print(err)
except IOError:
    print('error')
else:
    print('else')
finally:
    print('finally')
    
'''  
def ageFun(age):
    if(age<=18):
        raise Exception('not  aligible for vote',age)
    
# try:
#     ageFun(18)
# except Exception as err:
#     print(err)

# class Networkerror(RunTimeError):
#     def __init__(self,arg):
#         self.args =  arg
        
# try:
#     raise Networkerror('bad network')
# except Networkerror as net:
#     print(net)
    
    
for i in range(0,10,2):
    print(i)
    

# Sys command line concept
'''
import sys
import sys

if len(sys.argv)<2:
    print('please provide command line argument')
    sys.exit()
    
print('there are %d arguments '%len(sys.argv))
print('The command line argument')
print(sys.argv)
for  i in sys.argv:
    print(i)
print(sys.path)
sum = 0.0
for i in range(1,(len(sys.argv)),1):
    sum += float(sys.argv[i])
print(sum)

'''





try:
    fh = open('mice.txt','r')
    print('try')
    # fh.write('ss')
    fh.close()
except Exception as err:
    print(err)
# except IOError:
#     print('error')
else:
    print('else')
finally:
    print('finally')
    
    
def kelvinToFahrenhit(tempFahrenheit):
    assert(tempFahrenheit >= 0),"Colder than absolute zero"
    return ((tempFahrenheit - 273)*(9/5))+32
print(kelvinToFahrenhit(273))
print(kelvinToFahrenhit(505.75))
# print(kelvinToFahrenhit(-5))


import logging
logging.basicConfig(level = logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def fac(n):
    logging.debug('Start of factorial (%s%%)' %(n))
    total = 1
    for i in range(n+1):
        total *=i
        logging.debug('i is '+str(i) + ',total is '+str(total))
        logging.debug('End of factorial(%s%%' %(n))
        
    return total
logging.debug('start')
print(fac(5))
logging.debug('end')