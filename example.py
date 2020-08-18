import math
import random

# multiline code
a = 10
b = 20
print(a\
      +\
      b\
    )
#output 30
x = y = z =10
print(x,y,z)
y=25
print(x,y,z)


# ********************* DATA TYPE *****************************
# 1==> boolean
print(bool(not None))  #True
# False
print(bool(None))

print(bool(''))
print(bool(0))
print(bool(0))
print(bool(0.0))
print(bool(0j))
print(bool(()))
print(bool([]))
print(bool({}))

# 2==> numbers
s = 10
g =5.02
k = 0.222

print(s,g)
del s
del g,k

# print(s,g) shows error because del =>deleted s g variable

# int float  long(hexa & decimal can be used in) complex
m = 8 + 5j
print(m)
#  3==> STRING

string = "SWATHI ACHARYA "
print(string[0])
print(string[0:10])
print(string[0:])
print(string[5:9])
# print(string[-1:])
# print(string[-1])
# print(string[-1:0])
print(string + 'from surathkal')
print(string * 3)
# escape character
print('sss\a')
print('www\b')
print('hhhh \cx')
print('hp\C-x')
print('hhhh\e')
print('hhhh\f')
print('hhhh\M-\C-x')

# r/R raw string
print(r'\n jd reu  kjn')
print('\nhhh')

print(R'\n ff \n')

# IN ND NOT IN
if('h' in 'swathi'):
    print('true')
if('z' not in 'swathi'):
    print('true')

#  multiline
print("""hello
this 
is the the example 
for multiine""")

# STRING METHOD
st ="hello World"
print(st.capitalize())

print(st.center(3,'d'))

print(st.count('ll'))
print(st.find('o Wo'))
print(st.split('l'))
print(st.title())
print(st.isdecimal())

# 4==> LISTS MUTABLE
LST =[[1,2,3,4],['k','k','l'],[2,'l']]
print(LST)
#5==>>Tuple immutable
#6==>Set 
dict = {}
dict[1] ='a'
dict[2] = 'b'

print(dict)

print(dict.keys())

print(dict.values())

dictionary = {1:2,2:34,4:43}
print(dictionary)

#7==>set no dublicate value

print(set([1,1,1,2,3,4,4,4,5]))

print(set([1,1,1,2,3,4,4,4,5]))
set1 ={1,2,3}
set2 = {3,4,5}
print(set1)
print(set2)
print('union=> ',set1 | set2)
print('intersection ==> ',set1 & set2)

print('Difference ==> ',set1 - set2)

print('Symmetric difference==> ',set1 ^ set2)



# NUMBER TYPE CONVERSION
x = 52
print(x)
print('float',float(x))
# print('long ',long(x))
print('complex ',complex(x))
y = -25
print(abs(y))
# print(math.ceil(y))


# print(math.cmp(x,y))
# print(ceil(y))
print(random.choice(LST))
print(random.randrange(1,12,5))
print(random.random())
from random import shuffle
print(shuffle(LST))
print(LST)

# For loop
