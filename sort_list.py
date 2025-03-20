list = ['apple ', 'banana', 'cherry']
list.sort()
print(list)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

list = ['apple ', 'banana', 'cherry']
list.sort(reverse = True)
print(list)

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)