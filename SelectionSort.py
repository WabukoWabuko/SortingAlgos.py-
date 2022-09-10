import time as t
# Selection Sort function.


def Sort(List):
    length = len(List)

    for i in range(length-1):
        minIndex = i

        for j in range(i+1, length):
            if List[j] < List[minIndex]:
                minIndex = j

        List[i], List[minIndex] = List[minIndex], List[i]
    return List


list = [4, 8, 2, 4, 0, 1]
print("Unsorted List: ", list)
print("List in Ascending order")
t.sleep(3)
print("...")
t.sleep(2)
print("..")
t.sleep(1)
print(".")
t.sleep(2)
print("Sorted List: ", Sort(list))
