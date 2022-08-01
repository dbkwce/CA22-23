// NAME : DNYANESHWAR SHINDE
// PRN: 2020BTEIT00032
// COMPUTER ALGORITHMS ASSIGNMENT 1

#include <iostream>
using namespace std;
int totalComp = 0;

void swapNumbers(int &a, int &b)
{
    totalComp++;
    int t = a;
    a = b;
    b = t;
}

int partition(int arr[], int start, int end)
{

    int pivot = arr[start];

    int count = 0;
    for (int i = start + 1; i <= end; i++)
    {
        if (arr[i] <= pivot)
            count++;
    }

    int pivotIndex = start + count;
    swapNumbers(arr[pivotIndex], arr[start]);

    int i = start, j = end;

    while (i < pivotIndex && j > pivotIndex)
    {

        while (arr[i] <= pivot)
        {
            i++;
        }

        while (arr[j] > pivot)
        {
            j--;
        }

        if (i < pivotIndex && j > pivotIndex)
        {
            swapNumbers(arr[i++], arr[j--]);
        }
    }

    return pivotIndex;
}

void quickSort(int arr[], int start, int end)
{
    // cout << "quick sort " << endl;

    if (start >= end)
        return;

    int selectedPivot = partition(arr, start, end);

    quickSort(arr, start, selectedPivot - 1);

    quickSort(arr, selectedPivot + 1, end);
}

void printArray(int n, int a[])
{
    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
    cout << endl;
}

void takeInputArray(int n, int arr[])
{
    for (int i = 0; i < n; i++)
    {
        cin >> arr[i];
    }
}

int main()
{

    cout << "Enter the Size of Array : " << endl;
    int n;
    cin >> n;
    cout << "Enter the Elements of Array : " << endl;
    int arr[n];
    takeInputArray(n, arr);

    quickSort(arr, 0, n - 1);
    cout << "Sorted Array : " << endl;

    printArray(n, arr);
    cout << "Total comp or swaps : " << totalComp << endl;

    return 0;
}
