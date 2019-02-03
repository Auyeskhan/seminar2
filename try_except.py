# FileNotFoundError
def openfl(x):
  try:
    with open(x) as file:
      read_data = file.read()
  except:
    print('Ouch, Could not open file.log')
  
if __name__ == '__main__':
  print(openfl('file.log'))
