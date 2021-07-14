"""
INSERTION SORT
get value; loop through list, if value < future element
check each element to the left, if future element > than element to left. slide element to right slide future to left
repeat

1. Call insert to insert the element that starts at index 1 into the sorted subarray in index 0.
2. Call insert to insert the element that starts at index 2 into the sorted subarray in indices 0 through 1.
3. Call insert to insert the element that starts at index 3 into the sorted subarray in indices 0 through 2.
4. …
5. Finally, call insert to insert the element that starts at index n−1n−1n, minus,
   1 into the sorted subarray in indices 0 through n−2n−2n, minus, 2.

"""


def insertionSort(m):
    right_index = 1
    new_index = 0
    # Traverse through 1 to len(arr)
    for i in range(len(m)):

        key = m[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i - 1
        while j >= 0 and key < m[j]:
            m[j + 1] = m[j]
            j -= 1
        m[j + 1] = key
    return m


my_arr = [3, 5, 7, 11, 13, 2, 9, 6]

print('Result: [2, 3, 5, 6, 7, 9, 11, 13')
print(insertionSort(my_arr))