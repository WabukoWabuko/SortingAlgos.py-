import time as t
# Counting sort function.


def countingSort(array):
    size = len(array)
    output = [0] * size

    # Initialize count array
    count = [0] * 10

    # Store the count of each element in a count array
    for i in range(0, size):
        count[array[i]] += 1

    # Store the cumulative count
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Finding the position of each element of the original array in count array and placing the elements in output array
    i = size - 1
    while i >= 0:
        output[count[array[i]] - 1] = array[i]
        count[array[i]] -= 1
        i -= 1

    # Copying the sorted elements into original array
    for i in range(0, size):
        array[i] = output[i]


list = [4, 2, 2, 8, 3, 3, 1]
print("Unsorted List: ", list)
print("Array in Ascending order")
t.sleep(3)
print("...")
t.sleep(2)
print("..")
t.sleep(1)
print(".")
t.sleep(2)
countingSort(list)
print("Sorted List: ", list)
