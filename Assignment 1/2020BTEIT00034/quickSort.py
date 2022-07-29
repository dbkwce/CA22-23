"""
    Quick Sort
    ----------
    Daulatrao Patil - 2020BTEIT00034
    ----------

    Time Complexity: O(n log n)
    Space Complexity: O(log n)
    Stable: Yes

    Algorithm:
        1. Pick a pivot element
        2. Partition the array around the pivot element
        3. Recursively sort the subarrays

        Partition:
        --------------------
            1. Pick the last element as pivot
            2. Compare the pivot with all the elements in the array
            3. If the pivot is greater than the element, then move the pivot to the right
            4. If the pivot is less than the element, then move the pivot to the left
            5. Repeat the steps 2-4 until the pivot is at the right place
            6. Return the pivot position
"""

import random

def partition(A, low, high):
    pivot = A[high]
    i = low - 1

    for j in range(low, high):
        if A[j] <= pivot:
            i += 1
            A[i], A[j] = A[j], A[i]

    A[i+1], A[high] = A[high], A[i+1]

    return i+1

def quickSort(A, low, high):
    if low < high:
        pivot_ele = partition(A, low, high)

        quickSort(A, low, pivot_ele-1)
        quickSort(A, pivot_ele+1, high)
    else:
        return

def main():
    n = int(input())

    A = [random.randint(0, 1000) for i in range(n)]

    print("Unsorted array: ", A)

    quickSort(A, 0, n-1)

    print("Sorted array: ", A)
    
if __name__ == "__main__":
    main()