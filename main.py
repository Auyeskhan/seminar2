from mybox import MyBox
from myboxiterator import MyBoxIterator

b = MyBox()
b.add('hello')
b.add(1)
b.add(', ')
b.add(True)
b.add('Bob')
b.remove(True)
if(1 in b) and (len(b)>0):
  b.remove(1)
msg = ''
for bg in b:
  msg += bg
print(msg)
