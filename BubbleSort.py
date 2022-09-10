import time
# Bubble Sort function.


def bubble_sort(list1):
    # Outer loop for traversing the entire list
    for i in range(0, len(list1)-1):
        for j in range(len(list1)-1):
            # Checking larger element.
            if list1[j] > list1[j + 1]:
                # Swapping leftElement with rightElement
                temp = list1[j]
                list1[j] = list1[j+1]
                list1[j+1] = temp
    return list1
  

# List
list1 = [5, 3, 8, 0, 6, 7, 2]

print("Unsorted list: ", list1)

# Calling the bubble sort function
print("List in Ascending order")
time.sleep(3)
print("...")
time.sleep(2)
print("..")
time.sleep(1)
print(".")
time.sleep(2)
print("Sorted list: ", bubble_sort(list1))
