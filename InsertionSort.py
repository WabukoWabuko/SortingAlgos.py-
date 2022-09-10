import time as t
# Insertion sort in Python


def insertionSort(array):

    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        
        # Comparing key to each element on the left of it until an element smaller than it is found.
        # Descending order, change key<array[j] to key>array[j].
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        
        # Place key at after the element just smaller than it.
        array[j + 1] = key


data = [9, 5, 1, 4, 3, 6, 13, 27, 0]
print("Unsorted List: ", data)
insertionSort(data)
print("List in Ascending order")
t.sleep(3)
print("...")
t.sleep(2)
print("..")
t.sleep(1)
print(".")
t.sleep(2)
print("Sorted List: ", data)
