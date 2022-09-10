import time as t
# MergeSort in Python


def mergeSort(List):
    if len(List) > 1:

        #  r is a point where an List gets divided into two sub-Lists
        r = len(List)//2
        L = List[:r]
        M = List[r:]

        # Sort the two halves
        mergeSort(L)
        mergeSort(M)

        i = j = k = 0

        # Until we reach either end of L or M, pick the largest amongst
        # elements L and M and place them in the correct position at A[p..r]
        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                List[k] = L[i]
                i += 1
            else:
                List[k] = M[j]
                j += 1
            k += 1

        # When we run out of elements in either L or M,
        # pick up the remaining elements and put in A[p..r]
        while i < len(L):
            List[k] = L[i]
            i += 1
            k += 1

        while j < len(M):
            List[k] = M[j]
            j += 1
            k += 1


# Print the List
def printList(List):
    for i in range(len(List)):
        print(List[i], end=" ")
    print()


# Driver program
if __name__ == '__main__':
    List = [6, 5, 12, 10, 9, 1]
    print("Unsorted List: ", List)

    mergeSort(List)
    print("List in Ascending order")
    t.sleep(3)
    print("...")
    t.sleep(2)
    print("..")
    t.sleep(1)
    print(".")
    t.sleep(2)
    print("Sorted List: ", List)
