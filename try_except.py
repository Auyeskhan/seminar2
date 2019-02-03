# FileNotFoundError
def openfl(x):
  try:
    with open(x) as file:
      read_data = file.read()
  except:
    print('Ouch, Could not open file.log')
#IndexError
def lst(a):
  try:
    return abc[a]
  except:
    print("Out of index")

#KeyError
def keyer(b):
  try:
    return cba[b]
  except:
    print("key is not found in a dictionary")
  
if __name__ == '__main__':
# FileNotFoundError
  print(openfl('file.log'))
#IndexError
  abc=[1,2,3]
  print(lst(3))
#KeyError
  cba = { 'a':1, 'b':2 }
  print (keyer('c'))
