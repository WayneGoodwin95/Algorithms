"""
MERGE SORT
- divide
- conquer
- combine
"""

from math import floor, ceil


def mergeSort(arr):
    # Divide
    if len(arr) > 1:
        left_arr = arr[:len(arr)//2] # left array is 0 - midpoint
        right_arr = arr[len(arr)//2:] # right array is midpoint - last index of array

        # recursion - recursively loop through each side of array until array length is less than 1.
        #                   Only one element [0]. means its already sorted
        mergeSort(left_arr)
        mergeSort(right_arr)

        # merge // combine
        i = 0 # left array index
        j = 0 # right array index
        k = 0 # merged array index

        # loop while i and j have multiple elements
        while i < len(left_arr) and j < len(right_arr):
            # check which array has the lower value
            if left_arr[i] < right_arr[j]: # Left array is lower
                # place left array in original array
                arr[k] = left_arr[i]
                i += 1 # increment i as the left array element has been merged
            else: # right array is lower
                arr[k] = right_arr[j]
                j += 1 # increment j as the right arr element has been merged
            k += 1 # increment the merged array each loop as it is now assigned the lowest value from left or right

        # loop if only left array has multiple elements
        while i < len(left_arr):
            arr[k] = left_arr[i]
            i += 1
            k += 1

        # loop if only right array has multiple elements
        while j < len(right_arr):
            arr[k] = right_arr[j]
            j += 1
            k += 1


arr = [14, 7, 3, 12, 9, 11, 6, 2]
print('Original: ', arr)
mergeSort(arr)
print('Sorted:   ', arr, '\n')


arr2 = [1, 27, 3, 2, 5, 6, 45,4, 3, 6 ,78, 34]
print('Original: ', arr2)
mergeSort(arr2)
print('Sorted:   ', arr2, '\n')