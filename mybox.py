from myboxiterator import MyBoxIterator
class MyBox:
  def __init__(self):
    self._theItems = list()
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
  def __iter__(self,item):
    return MyBoxIterator (self._theItems)
