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
    returnvself._theItems.pop(idx)
  def __contains__(self,item):
    return item in self._theItems
  def __iter__(self,item):
    return BagIterator (self._theItems)

class BagIterator():
  def __init__( self, L ):
    self.L = L # the list
    self.idx = 0 # curent item
  def __iter__(self):
    return self
  def __next__(self):
    if self.idx < len(self.L):
      item = self.L[self.idx]
      self.idx += 1
      return item
    else:
      raise StopIteration
