dic = dict()
print(type(dic))

dic = {
    1:1,
    2:34,
    5:['l','t'],
    3:(2,3),
    4:{5,53}
}
print(dic)
print(type(dic[3]))

for key in dic.keys():
    print(key)
for item in dic.items():
    print(item)

for values in dic.values():
    print(key)
for key, value in dic.items():
    print('key {} ---> value {} '.format( key, value))

dic[1]= 'newvalue 1'
print(dic)
dic.update({'k':'kk'})
print(dic)
val = dic.pop(1)
print(val)
print(dic)
val = dic.get(5)
print(val)
# print(dic)
val = dic.copy()
print(val)


for key, value in val.items():
    print('key {} ---> value {} '.format( key, value))

