listValue = [0, 1, 2,3,4]
ip = int(input())
for i in listValue:
    if ip == i:
        print('if inside list')
        break
else:
    print("elses")
while ip:
    print(ip)
    break
else:
    print("Else")

listvalue =['a','c','t','y']
print(listvalue)
print(listvalue[0])

print(listvalue[-1:-2])

print(listvalue[-1:2])





c = listvalue.index('a')
print(c)


c = listvalue.count('a')
print(c)

# del listvalue[3]
# listvalue.remove('a')

# listValue.pop()

# print(listvalue)
listValue.append('k')

# print(listvalue)
listValue.extend('e')
# print(listvalue)
# listValue.insert(listvalue[0])

# print(listvalue)
listValue.insert(3,'ip')


print(listValue)

print(listValue[0:-2])
print(listValue[-5:-1])
print(listValue[0:-2])

print(listValue[:-1])
print(listValue[::-1])


sum = lambda a1, a2, a3: a1+a2+a3;

print(sum(10,20,30))












