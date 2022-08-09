#include<stdio.h>
#include <cstdlib>
// declare global variable counter
int counter = 0;

void swap(int *a, int *b);


// partition
int partition(int arr[], int low, int high)
{
    int pivot = arr[high];
    int i = (low - 1);
    for (int j = low; j <= high - 1; j++)
    {
        counter++;
        if (arr[j] < pivot)
        {
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]);
    return (i + 1);
}

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
// quick sort
void quickSort(int arr[], int low, int high)
{
    if (low < high)
    {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}



// main
int main(){
    int a[10000];
    for(int i = 0; i < 10000; i++){
        a[i] = i+1;
    }
    quickSort(a, 0, 10000-1);
    // print array
    for(int i = 0; i < 10000; i++){
        printf("%d ", a[i]);
    }
    printf("%d\n", counter);
    return 0;

}
