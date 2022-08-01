//Write a modular algorithm "Quick sort" with at least three functions(modules) for sorting given n numbers.
//PRN-2020BTEIT00025
//Name-Harshad Hanamant Jagadale
#include<iostream>
using namespace std;

void qsort(int[], int, int);
int  breakdown(int[], int, int);
void swapping(int*, int*);

int main()
{
    int n,i;

    printf("Enter array size:\n");
    scanf("%d",&n);

    int array[n];

     
    for(i=0;i<n;i++)
       { array[i]=rand();
       }
    quickSort(array,0,n-1);

    printf("After QuickSort:\n");

    for(i=0;i<n;i++)
        printf("%d ",array[i]);
    printf("\n");

    return 0;
}

void qsort(int array[], int start, int end)
{
    if(start < end)
    {
        int pIndex = partition(array, start, end);
        quickSort(array, start, pIndex-1);
        quickSort(array, pIndex+1, end);
    }
}

int breakdown(int array[], int start, int end)
{
    int pIndex = start;
    int pivot = array[end];
    int i;
    for(i = start; i < end; i++)
    {
        if(arr[i] < pivot)
        {
            swap(&array[i], &array[pIndex]);
            pIndex++;
        }
    }
    swap(&arr[end], &arr[pIndex]);
    return pIndex;
}

void swapping(int *x, int *y)
{
    int t = *x;
    *x = *y;
    *y = t;
}