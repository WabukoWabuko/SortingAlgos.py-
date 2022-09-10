import time as t
# Bucket Sort function in Python.


def bucketsorting(List):
    bucket = []

    # Creating empty buckets
    for i in range(len(List)):
        bucket.append([])

    # Inserting elements into respective buckets
    for j in List:
        index_b = int(10 * j)
        bucket[index_b].append(j)

    # Sorting elements of each bucket
    for i in range(len(List)):
        bucket[i] = sorted(bucket[i])

    # Getting sorted elements
    k = 0
    for i in range(len(List)):
        for j in range(len(bucket[i])):
            List[k] = bucket[i][j]
            k += 1
    return List


List = [.33, .52,.42, .32, .37, .47, .51]
print("Unsorted List: ", List)
print("List in Ascending order")
t.sleep(3)
print("...")
t.sleep(2)
print("..")
t.sleep(1)
print(".")
t.sleep(2)
print("Sorted List: ", bucketsorting(List))
