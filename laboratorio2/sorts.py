# BUBBLE SORT

def bubble_sort(arr):
    n = len(arr)
    count = 0

    for i in range(n - 1):
        for j in range(0, n - i - 1):
            count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return count, arr  # Devuelve el contador de comparaciones al final del algoritmo.

# HEAP SORT

"""
Código extraído de: https://www.geeksforgeeks.org/heap-sort/
"""

def heapify(arr, N, i):
    count = 1
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < N and arr[largest] < arr[l]:
        largest = l

    if r < N and arr[largest] < arr[r]:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        count += heapify(arr, N, largest)

    return count

def heap_sort(arr):
    N = len(arr)
    count = 0

    for i in range(N // 2 - 1, -1, -1):
        count += heapify(arr, N, i)

    for i in range(N - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        count += heapify(arr, i, 0)

    return count, arr

# INSERTION SORT

def insertion_sort(arr):
    count = 0

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            count += 1
        arr[j + 1] = key
        count += 1

    return count, arr

# SELECTION SORT

def selection_sort(arr):
  count = 0
  for i in range(len(arr)):
      count += 1
      curr = i
      for j in range(i + 1, len(arr)):
          count += 1
          if arr[curr] > arr[j]:
              count += 1
              curr = j
      arr[i], arr[curr] = arr[curr], arr[i]

  return count, arr


# SHELL SORT

"""
Código extraído de: https://www.geeksforgeeks.org/shellsort/
"""

def shell_sort(arr):
    # code here
    n = len(arr)
    gap=n//2
    count = 0

    while gap>0:
        count += 1
        j=gap
        # Check the array in from left to right
        # Till the last possible index of j
        while j<n:
            count += 1
            i=j-gap # This will keep help in maintain gap value

            while i>=0:
                count += 1
                # If value on right side is already greater than left side value
                # We don't do swap else we swap
                if arr[i+gap]>arr[i]:
                    break
                else:
                    count += 1
                    arr[i+gap],arr[i]=arr[i],arr[i+gap]

                i=i-gap # To check left side also
                            # If the element present is greater than current element
            j+=1
        gap=gap//2

    return count, arr

# MERGE SORT

def merge_sort(arr):

    if len(arr) <= 1:
        return 0, arr  # Devuelve 0 comparaciones y el arreglo original si está vacío o tiene un solo elemento

    # Divide la lista en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Llama a merge_sort de forma recursiva en ambas mitades
    count_left, left_half = merge_sort(left_half)
    count_right, right_half = merge_sort(right_half)

    count_merge, sorted_arr = merge(left_half, right_half)  # Llama a una función auxiliar para fusionar y contar

    total_count = count_left + count_right + count_merge  # Suma los conteos de comparaciones

    return total_count, sorted_arr

def merge(left, right):
    count = 0
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        count += 1
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return count, result

# QUICK_SORT

"""
Código extraído de: https://www.geeksforgeeks.org/quick-sort/
"""

def partition(array, low, high, contador):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        contador[0] += 1  # Incrementar el contador en cada comparación
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def start_quick_sort(array, low, high, contador):
    if low < high:
        pi = partition(array, low, high, contador)
        start_quick_sort(array, low, pi - 1, contador)
        start_quick_sort(array, pi + 1, high, contador)

def quick_sort(arr):
    N = len(arr)
    contador = [0]  # Inicializar el contador en 0
    start_quick_sort(arr, 0, N - 1, contador)
    return contador[0], arr  # Devolver el arreglo ordenado y el contador de operaciones