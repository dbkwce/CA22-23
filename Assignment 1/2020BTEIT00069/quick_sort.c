/*
Name: Nidhish Chauhan
PRN No.: 2020BTEIT00069
Dept.: I.T.
*/

#include <stdio.h>
#include <stdlib.h>

void swap(int *x, int *y)
{
    printf("Inside swap()\n");
    int temp = *x;
    *x = *y;
    *y = temp;
}
int partition(int A[], int l, int h)
{

    printf("Inside partition()\n");
    int pivot = A[l];
    int i = l, j = h;

    do
    {
        do
        {
            i++;
        } while (A[i] <= pivot);
        do
        {
            j--;
        } while (A[j] > pivot);

        if (i < j)
            swap(&A[i], &A[j]);
    } while (i < j);

    swap(&A[l], &A[j]);
    return j;
}
void QuickSort(int A[], int l, int h)
{

    printf("Inside QuickSort()\n");
    int j;

    if (l < h)
    {
        j = partition(A, l, h);
        QuickSort(A, l, j);
        QuickSort(A, j + 1, h);
    }
}
int main()
{

    printf("Inside main()\n");
    // int n;
    int n = 10000;
    //* n=1e4 or 10000 will produce significant result in output file
    // scanf("%d", &n);
    int A[n];

    for (int i = 0; i < n; i++)
    {
        if (i % 2 == 0)
        {
            A[i] = i / 2;
            continue;
        }
        else if (i % 3 == 0)
        {
            A[i] = i * 3;
            continue;
        }
        A[i] = i;
    }

    printf("Before Sorting: \n");
    for (int i = 0; i < sizeof(A) / sizeof(A[0]); i++)
        printf("%d ", A[i]);

    QuickSort(A, 0, sizeof(A) / sizeof(A[0]));

    printf("\nAfter Sorting: \n");
    for (int i = 0; i < sizeof(A) / sizeof(A[0]); i++)
        printf("%d ", A[i]);

    printf("\n");

    return 0;
}