items = [0,1,2,3,4,5,6]

a = slice(2, 4)
print(items[2:4])
print(items[a])

print('-'*50)

items[a] = [10,11]
print(items)

del items[a]
print(items)


a = slice(1,3)
print(a.start)
print(a.stop)
print(a.step)

print('*'*50)
s = 'HelloWorld'
print(a.indices(len(s)))
for i in range(*a.indices(len(s))):
    print(s[i])