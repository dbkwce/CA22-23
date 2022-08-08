#include <bits/stdc++.h>

using namespace std;

// 9 4 5 7 3 10 8 2 1 6
// * /                \        

void quickSort(int ar[], int size, int pivot, int start, int end)
{

    if (start < end)
    {
        int piv = partitionFunction(ar, pivot, start, end);
        quickSort(ar, size, pivot, start, end);
    }
}

int partitionFunction(int ar[], int pivot, int start, int end)
{
    while (start < end)
    {
        while (ar[start] < ar[pivot])
        {
            start++;
        }

        while (ar[end] > ar[pivot])
        {
            end--;
        }

        swap(ar[end], ar[pivot]);
    }
}

int main()
{
    int n;

    cout << "Enter size of the Array: ";
    cin >> n;

    int ar[n];

    cout << "Enter the elements of the array:\n";
    for (int i = 0; i < n; i++)
    {
        ar[i] = rand();
    }

    quickSort(ar, n);

    cout << "Sorted Array: \n";
    for (int i = 0; i < n; i++)
    {
        cout << ar[i] << " ";
    }

    cout << endl;

    return 0;
}
