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


