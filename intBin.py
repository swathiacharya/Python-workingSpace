print(20 << 2)
print(bin(20))

print(-20 << 2)
print(bin(-20))

print("***************  Compliment ==> formula is  that ~x =  -x - 1  ***********")
a = 80
print('a ={}  ,  ~a = {} '.format(a,~a))

print("***************  Left bitwise shift  ***********")
a = -20 
n = 2
print('{} << {} == {} '.format(a, n, a<<n))
print(bin(-20))

print("***************************   BINARY TO INT      **********************************************")
print("***************************   RECURTION METHOD     **********************************************")
def binary(n):
    if(n>1):
        binary(n//8)
    print(n % 8,end='')
binary(20)
print()
# print(" \n ***************************   ITERATION METHOD     **********************************************")
# def binaryIteration(n):
#     for i =  1<<31; i>0; i=i/2
#         print(1) if (n & i) else print(0)
# binaryIteration(10)
print(oct(20))
print(type(oct(20)))

print("int to oct")
def octa(n):
    if(n>1):
        octa(n//16)
    print(n % 8,end='')
octa(20)
print()
print("int to hex")
def hexaDecimal(n):
    if(n>1):
        hexaDecimal(n//16)
    print(n % 16,end='')
hexaDecimal(20)
print()
print(hex(20))
print(type(hex(20)))