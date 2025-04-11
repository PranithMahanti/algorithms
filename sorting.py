# Basic swap mechanism 
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr

# Simple Sort
def simple_sort(arr):
    if len(arr) < 2:
        return arr
    maximum = arr[0]
    for item in arr:
        if maximum < item:
            maximum = item

    arr = swap(arr, arr.index(maximum), len(arr)-1)
    return simple_sort(arr[:len(arr)-1]) + [maximum]

# Quick Sort
def quick_sort(list):
    if len(list) < 2:
        return list
    pivot = list[0]
    lesser = [i for i in list if i<pivot]
    greater = [i for i in list if i>pivot]

    return quick_sort(lesser) + [pivot] + quick_sort(greater)

# Bubble Sort
def bubble_sort(arr):
    swapped = True
    while swapped:
        swapped = False
        for k in range(len(arr)-1):
            if arr[k] > arr[k+1]:
                arr = swap(arr, k, k+1)
                swapped = True

    return arr


