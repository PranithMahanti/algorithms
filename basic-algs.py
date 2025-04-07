# Grokking Algorithms - Practice
# By: promethei
# Start: 05 April 2025

# Binary Search
def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low<=high:
        mid = int((low+high)/2)
        guess = list[mid]

        if guess == item:
            return mid
        elif guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None

# Selection Sort
def selection_sort(list):
    sorted_list = []

    while list:
        smallest = list[0]
        smallest_index = 0
        for i in range(len(list)):
            if list[i] < smallest:
                smallest = list[i]
                smallest_index = i
        sorted_list.append(smallest)
        list.pop(smallest_index)
    
    return sorted_list

# Divide and Conquer for sum of list items
def dc_sum(list):
    if not list:
        return 0
    
    sum = list.pop(0) + dc_sum(list)
    return sum

# Divide and Conquer for maximum of list items
def dc_max_run(list):
    global max
    max = 0
    def dc_max(list):
        global max
        if list:
            if list[0] >= max:
                max = list.pop(0)
                dc_max(list)
            else:
                list.pop(0)
        return max
    
    return dc_max(list)


# Quick Sort
def quick_sort(list):
    if len(list) < 2:
        return list
    
    pivot = list[0]
    lesser = [i for i in list if i<pivot]
    greater = [i for i in list if i>pivot]

    return quick_sort(lesser) + [pivot] + quick_sort(greater)

