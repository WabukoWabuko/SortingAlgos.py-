import time as t

# Quick sort function.


def partition(List, low, high):

    # choose the rightmost element as pivot
    pivot = List[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if List[j] <= pivot:
            # if element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # swapping element at i with element at j
            (List[i], List[j]) = (List[j], List[i])

    # swap the pivot element with the greater element specified by i
    (List[i + 1], List[high]) = (List[high], List[i + 1])

    # return the position from where partition is done
    return i + 1


# function to perform quicksort


def quickSort(List, low, high):
    if low < high:

        # find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(List, low, high)

        # recursive call on the left of pivot
        quickSort(List, low, pi - 1)

        # recursive call on the right of pivot
        quickSort(List, pi + 1, high)


data = [8, 7, 2, 1, 0, 9, 6]
print("Unsorted List: ", data)
print("List in Ascending order")
t.sleep(3)
print("...")
t.sleep(2)
print("..")
t.sleep(1)
print(".")
t.sleep(2)
size = len(data)

quickSort(data, 0, size - 1)

print("Sorted List: ", data)
