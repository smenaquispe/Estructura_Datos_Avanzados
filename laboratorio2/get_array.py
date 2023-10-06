# get an array in base of the file
def get_array(size):
  arr = []
  with open("data.txt", 'r') as f:
    i = 0
    for line in f:
      if i == size:
        break
      arr.append(float(line))
      i += 1
  return arr