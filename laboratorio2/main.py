from get_time import get_time
from get_array import get_array
from sorts import *

sizes = []
for i in range(1, 500001):
  sizes.append(i)

bubble_counts = []
heap_counts = []
insertion_counts = []
selection_counts = []
shell_counts = []
merge_counts = []
quick_counts = []

check_points = [100, 1000, 10000, 100000]

for size in sizes:
  arr = get_array(size)

  c1, _, t1 = get_time(bubble_sort , arr.copy())
  c2, _, t2 = get_time(heap_sort, arr.copy())
  c3, _, t3 = get_time(insertion_sort, arr.copy())
  c4, _, t4 = get_time(selection_sort, arr.copy())
  c5, _, t5 = get_time(shell_sort, arr.copy())
  c6, _, t6 = get_time(merge_sort, arr.copy())
  c7, _, t7 = get_time(quick_sort, arr.copy())

  bubble_counts.append(c1)
  heap_counts.append(c2)
  insertion_counts.append(c3)
  selection_counts.append(c4)
  shell_counts.append(c5)
  merge_counts.append(c6)
  quick_counts.append(c7)

  if size in check_points:
    print(f"Tiempo medio en {size} elementos")
    print(f"Bubble sort: {t1}")
    print(f"Heap sort: {t2}")
    print(f"Insertion sort: {t3}")
    print(f"Selection sort: {t4}")
    print(f"Shell sort: {t5}")
    print(f"Merge sort: {t6}")
    print(f"Quick sort: {t7}")


    print("\n\n")