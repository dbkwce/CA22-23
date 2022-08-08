#include <iostream>
using namespace std;

void swap(int &a, int &b)
{
    int temp = a;
    a = b;
    b = temp;
}

int part(int arr[], int start, int end)
{

    int pivot = arr[start];

    int cnt = 0;
    for (int i = start + 1; i <= end; i++)
    {
        if (arr[i] <= pivot)
        {
            cnt++;
        }
    }

    int pivotI = start + cnt;
    swap(arr[pivotI], arr[start]);

    int i = start, j = end;

    while (i < pivotI && j > pivotI)
    {

        while (arr[i] <= pivot)
        {
            i++;
        }

        while (arr[j] > pivot)
        {
            j--;
        }

        if (i < pivotI && j > pivotI)
        {
            swap(arr[i++], arr[j--]);
        }
    }

    return pivotI;
}

void quickSort(int arr[], int start, int end)
{
    if (start >= end)
        return;
    int p = part(arr, start, end);

    quickSort(arr, start, p - 1);

    quickSort(arr, p + 1, end);
}

int main()
{

    int arr[10] = {9, 8, 7, 6, 5, 4, 3, 2, 1, 0};
    int n = 10;

    quickSort(arr, 0, n - 1);

    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }

    cout << endl;

    return 0;
}