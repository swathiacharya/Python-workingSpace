s1 = {12}
print(type(s1))
s1.add(1)

print(s1)

s1.update([2,5,55])
print(s1)
# delete
s1.discard(2)
print(s1)

s1.pop()
print(s1)

s1.remove(12)
print(s1)
s1.clear()
print(s1)