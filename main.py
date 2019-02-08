from mybox import MyBox
from myboxiterator import MyBoxIterator
from myclass import MyClass
b = MyBox()
b.add(MyClass('Auyeskhan', 'Kostanay', 'Teacher'))
b.add(MyClass('John', 'London', 'Writer'))
b.add(MyClass('Shamel', 'Kostanay', 'Student'))

b.remove(1)
for i in b:
      i.meth_1()
 
