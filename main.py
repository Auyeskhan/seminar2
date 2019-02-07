from mybox import MyBox
from myboxiterator import MyBoxIterator

b = MyBox('Auyeskhan', 'Kostanay', 'Teacher')
b.add('hello')

b.meth_1()

b.add('1234')
b.remove('hello')
for i in b:
      print(i)
