from myboxiterator import MyBoxIterator

class MyBox:
  def __init__(self):
    self._theItems = list()
  def __len__(self):
    return len(self._theItems)
  def add(self,item):
    self._theItems.append(item)
  def remove(self,item):
    self._theItems.pop(item)
  def __contains__(self,item):
    return item in self._theItems
  def __iter__(self):
    return MyBoxIterator (self._theItems)
