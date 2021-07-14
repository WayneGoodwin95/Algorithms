"""
SELECTION SORT
loop through list keeping track of smallest unchecked index (min_index)
if another index is smaller swap the value to min_index
once looped through, change the minimum index to the next array element
repeat
"""


def selectionSort(my_arr):
    min_index = 0
    for min_index in range(len(my_arr)):
        min_value = my_arr[min_index]
        for j in range(min_index, len(my_arr)):
            if my_arr[j] < my_arr[min_index]:
                min_value = my_arr[j]
                my_arr[j] = my_arr[min_index]
                my_arr[min_index] = min_value
    return my_arr



my_arr = [22, 11, 99, 88, 9, 7, 42]

print('output [7, 9, 11, 22, 42, 88, 99]')
print(selectionSort(my_arr))
