from myboxiterator import MyBoxIterator
from myclass import MyClass
class MyBox(MyClass):
  def __init__(self, surname, city, profession):
    self._theItems = list()
    MyClass.__init__(self, surname, city, profession)
  def __len__(self):
    return len(self._theItems)
  def add(self,item):
    self._theItems.append(item)
  def remove(self,item):
    assert item in self._theItems
    idx = self._theItems.index(item)
    return self._theItems.pop(idx)
  def __contains__(self,item):
    return item in self._theItems
  def __iter__(self):
    return MyBoxIterator (self._theItems)
