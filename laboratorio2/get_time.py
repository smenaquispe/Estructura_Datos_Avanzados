import time

# get the time in seconds of a process
def get_time(func, arr):
  start = time.time()
  c, _ = func(arr)
  end = time.time()

  return c, _, end - start