#include <iostream>
#include <stdlib.h>
using namespace std;

// Swap elements by reference
void swap(int *x, int *y)
{
    int temp = *x;
    *x = *y;
    *y = temp;
}

// dividing array into smaller parts
int Dividing(int A[], int l, int h)
{
    // assigning element at lowest index as pivot
    int pivot = A[l];

    // take two pointers to iterate through array
    int i = l, j = h;

    do
    {
        // increment the low pointer till we got element greater than pivot
        do
        {
            i++;
        } while (A[i] <= pivot);
        // decrement the high pointer till we got element smaller than pivot
        do
        {
            j--;
        } while (A[j] > pivot);

        // swap the elements at low and high pointer if low is less than high
        if (i < j)
            swap(&A[i], &A[j]);
    } while (i < j);
    // repeate the above procedure till low doesn't exceeds high

// swap pivot element and element at position j
    swap(&A[l], &A[j]);

    return j;
    // j will help to divide the array
    // elements left to index j are smaller than element at j
    // elements right to index j are greater than element at j
}

void QuickSort(int A[], int l, int h)
{
    // take a pointer
    int j;

    if (l < h)
    {
        // get the index of Dividing
        j = Dividing(A, l, h);

        // sort left side of j
        QuickSort(A, l, j);

        // sort right side of j
        QuickSort(A, j + 1, h);
    }
}

int main()
{
    int A[] = {11, 13, 7, 12, 16, 9, 24, 5, 10, 3};
    int n = 10, i;
    QuickSort(A, 0, n);
    for (i = 0; i < 10; i++)
        printf("%d ", A[i]);
    printf("\n");
    return 0;
}