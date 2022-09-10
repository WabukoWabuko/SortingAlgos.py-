import time as t
# Shell sort function.


def Sort(List, n):

    # Rearrange elements at each n/2, n/4, n/8, ... intervals
    interval = n // 2
    while interval > 0:
        for i in range(interval, n):
            temp = List[i]
            j = i
            while j >= interval and List[j - interval] > temp:
                List[j] = List[j - interval]
                j -= interval

            List[j] = temp
        interval //= 2


data = [9, 8, 3, 7, 5, 6, 4, 1]
print("Unsorted List: ", data)
print("Array in Ascending order")
t.sleep(3)
print("...")
t.sleep(2)
print("..")
t.sleep(1)
print(".")
t.sleep(2)
size = len(data)
Sort(data, size)
print("Sorted List: ", data)
